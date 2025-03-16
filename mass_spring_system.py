import numpy as np

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
        """Runs the simulation and returns the results."""
        steps = int(t_max / dt)
        state = np.array([*self.mass.position, *self.mass.velocity])
        positions = []
        for _ in range(steps):
            positions.append(state[:2])
            state = self.runge_kutta_step(state, dt)
            self.mass.position = state[:2]
            self.mass.velocity = state[2:]
        return np.array(positions)

