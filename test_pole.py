from manimlib import *
import numpy as np

# 添加球坐标转换函数
def spherical_to_cartesian(r, phi, theta):
    """球坐标转笛卡尔坐标
    Args:
        r: 半径
        phi: 方位角 (绕z轴旋转，0-2π)
        theta: 极角 (与z轴夹角，0-π)
    """
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return np.array([x, y, z])

class magnet(Scene):
    def construct(self):
        # 创建左右两个点
        left_dot = Dot(LEFT * 3)
        right_dot = Dot(RIGHT * 3)
        
        # 添加放射光线（数量可调）
        num_rays = 120  # 将数量从12大幅增加到48
        
        def create_rays(dot, num):
            rays = VGroup()
            for i in range(num):
                angle = 2 * PI * i / num
                # 使用球坐标系生成3D方向
                dir = spherical_to_cartesian(1, angle, PI/4)
                # 修改光线长度为5倍方向向量（原为0.5）
                ray = Line(dot.get_center(), dot.get_center() + dir * 5)
                ray.set_stroke(WHITE, width=1)
                rays.add(ray)
            return rays
        
        left_rays = create_rays(left_dot, num_rays)
        right_rays = create_rays(right_dot, num_rays)
        
        # 显示两个点和光线
        self.play(ShowCreation(left_dot), ShowCreation(right_dot))
        self.play(ShowCreation(left_rays), ShowCreation(right_rays))
        self.wait()