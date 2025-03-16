import numpy as np
import os

class Mass:
    """Represents a mass connected to the spring."""
    def __init__(self, position, velocity, mass):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.mass = mass

class Spring:
    """Represents a spring with a rest length and spring constant."""
    def __init__(self, k, rest_length):
        self.k = k
        self.rest_length = rest_length

class System:
    """Simulates the mass-spring system in two dimensions."""
    def __init__(self, mass, spring, damping=0.0):
        self.mass = mass
        self.spring = spring
        self.damping = damping  # Damping coefficient

    def force(self):
        """Calculates the spring force on the mass."""
        displacement = np.linalg.norm(self.mass.position) - self.spring.rest_length
        direction = -self.mass.position / np.linalg.norm(self.mass.position)
        spring_force = self.spring.k * displacement * direction
        damping_force = -self.damping * self.mass.velocity
        return spring_force + damping_force

    def derivatives(self, state):
        """Calculates the derivatives for the RK4 method."""
        position = np.array([state[0], state[1]])
        velocity = np.array([state[2], state[3]])
        acceleration = self.force() / self.mass.mass
        return np.array([velocity[0], velocity[1], acceleration[0], acceleration[1]])

    def runge_kutta_step(self, state, dt):
        """Applies one step of the RK4 method."""
        k1 = self.derivatives(state)
        k2 = self.derivatives(state + 0.5 * dt * k1)
        k3 = self.derivatives(state + 0.5 * dt * k2)
        k4 = self.derivatives(state + dt * k3)
        return state + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

    def simulate(self, t_max, dt):
        """Run the simulation and saves the data to 'data/data.dat"""
        steps = int(t_max / dt)
        state = np.array([*self.mass.position, *self.mass.velocity])
        os.makedirs("data", exist_ok=True)

        with open("data/data.dat", "w") as file: 
            file.write("# t x y vx vy E_kin E_pot E_total\n")
            time = 0.0
            x, y, vx, vy = state

            kinetic_energy = 0.5 * self.mass.mass * (vx**2 + vy**2)

            # Elastic potencial energy: (1/2) * k * (ΔL)^2
            displacement = np.linalg.norm(self.mass.position) - self.spring.rest_length
            potential_energy = 0.5 * self.spring.k * displacement**2

            total_energy = kinetic_energy + potential_energy

            file.write(f"{time:.5f} {x:.5f} {y:.5f} {vx:.5f} {vy:.5f} {kinetic_energy:.5f} {potential_energy:.5f} {total_energy:.5f}\n")

            # Advance simulation
            state = self.runge_kutta_step(state, dt)
            self.mass.position = state[:2]
            self.mass.velocity = state[2:]
            time += dt
