import auto_py_to_exe.utils
import numpy as np
import matplotlib.pyplot as plt

g = 9.81

def get_input():
    height = float(input("Введите высоту (в метрах): "))
    initial_velocity = float(input("Введите начальную скорость (в м/с): "))
    angle_degrees = float(input("Введите угол (в градусах): "))
    return height, initial_velocity, np.radians(angle_degrees)

def calculate_trajectory(height, v, ang):
    t_max = (v * np.sin(ang) + np.sqrt((v * np.sin(ang))**2 + 2 * g * height)) / g
    t = np.linspace(0, t_max, num=500)

    x = v * np.cos(ang) * t
    y = height + v * np.sin(ang) * t - 0.5 * g * t**2
    v_x = np.full_like(t, v * np.cos(ang))
    v_y = v * np.sin(ang) - g * t
    speed = np.sqrt(v_x**2 + v_y**2)

    return t, x, y, v_x, v_y, speed

def plot_all_graphs(t, x, y, speed):
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))

    # Траектория
    axs[0, 0].plot(x, y, label="Траектория", color='b')
    axs[0, 0].set_title("Траектория движения")
    axs[0, 0].set_xlabel("X (м)")
    axs[0, 0].set_ylabel("Y (м)")
    axs[0, 0].legend()
    axs[0, 0].grid(True)

    # Скорость от времени
    axs[0, 1].plot(t, speed, label="Скорость", color='r')
    axs[0, 1].set_title("Зависимость скорости от времени")
    axs[0, 1].set_xlabel("Время (с)")
    axs[0, 1].set_ylabel("Скорость (м/с)")
    axs[0, 1].legend()
    axs[0, 1].grid(True)

    # Координаты от времени
    axs[1, 0].plot(t, x, label="X", color='g')
    axs[1, 0].plot(t, y, label="Y", color='m')
    axs[1, 0].set_title("Зависимость координат от времени")
    axs[1, 0].set_xlabel("Время (с)")
    axs[1, 0].set_ylabel("Координаты (м)")
    axs[1, 0].legend()
    axs[1, 0].grid(True)

    plt.tight_layout()
    plt.show()

def main():
    height, initial_velocity, angle = get_input()
    t, x, y, v_x, v_y, speed = calculate_trajectory(height, initial_velocity, angle)

    plot_all_graphs(t, x, y, speed)

if __name__ == "__main__":
    main()
