import numpy as np
import os


class Mass:
    """Representa una masa conectada al resorte."""
    def __init__(self, position, velocity, mass):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.mass = mass

class Spring:
    """Representa un resorte con una longitud en reposo y una constante de resorte."""
    def __init__(self, k, rest_length):
        self.k = k
        self.rest_length = rest_length

class System:
    """Simula el sistema masa-resorte en dos dimensiones."""
    def __init__(self, mass, spring, damping=0.0):
        self.mass = mass
        self.spring = spring
        self.damping = damping  # Coeficiente de amortiguamiento

    def force(self):
        """Calcula la fuerza del resorte sobre la masa."""
        displacement = np.linalg.norm(self.mass.position) - self.spring.rest_length
        direction = -self.mass.position / np.linalg.norm(self.mass.position)
        spring_force = self.spring.k * displacement * direction
        damping_force = -self.damping * self.mass.velocity
        return spring_force + damping_force

    def derivatives(self, state):
        """Calcula las derivadas para el método RK4."""
        position = np.array([state[0], state[1]])
        velocity = np.array([state[2], state[3]])
        acceleration = self.force() / self.mass.mass
        return np.array([velocity[0], velocity[1], acceleration[0], acceleration[1]])

    def runge_kutta_step(self, state, dt):
        """Aplica un paso del método RK4."""
        k1 = self.derivatives(state)
        k2 = self.derivatives(state + 0.5 * dt * k1)
        k3 = self.derivatives(state + 0.5 * dt * k2)
        k4 = self.derivatives(state + dt * k3)
        return state + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

    def simulate(self, t_max, dt, datapath="data.dat"):
        """Ejecuta la simulación y guarda los datos en 'data/data.dat'"""
        steps = int(t_max / dt)
        state = np.array([*self.mass.position, *self.mass.velocity])
        os.makedirs("data", exist_ok=True)

        with open(f"data/{datapath}", "w") as file:
            file.write("# t x y vx vy E_kin E_pot E_total\n")
            time = 0.0
            for _ in range(steps):
                x, y, vx, vy = state

                kinetic_energy = 0.5 * self.mass.mass * (vx**2 + vy**2)

                # Energía potencial elástica: (1/2) * k * (ΔL)^2
                displacement = np.linalg.norm(self.mass.position) - self.spring.rest_length
                potential_energy = 0.5 * self.spring.k * displacement**2

                total_energy = kinetic_energy + potential_energy
                data_str = f"{time:.5f} {x:.5f} {y:.5f} {vx:.5f} {vy:.5f} {kinetic_energy:.5f} {potential_energy:.5f} {total_energy:.5f}\n"

                file.write(data_str)

                state = self.runge_kutta_step(state, dt)
                self.mass.position = state[:2]
                self.mass.velocity = state[2:]
                time += dt

if __name__ == "__main__": 
    # System parameters: 
    mass = Mass(position=[1.0, 0.0], velocity=[1.0, 2.0], mass=1.0)
    spring = Spring(k=10.0, rest_length=1.0)
    system_damped = System(mass=mass, spring=spring, damping=0.1)
    system_regular = System(mass=mass, spring=spring, damping=0.0)
    # Simulation parameters
    t_max = 20.0
    dt = 0.01
    system_damped.simulate(t_max, dt, datapath="damped_data.dat")
    system_regular.simulate(t_max, dt, datapath="regular_data.dat")
