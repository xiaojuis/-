"""
傅科摆模拟程序的主脚本
"""
import matplotlib.pyplot as plt
from visualization import PendulumAnimator
from config_reader import read_simulation_parameters

def main():
    """主函数，运行模拟程序"""
    try:
        # 从配置文件读取参数
        params = read_simulation_parameters()
        
        print("\n正在初始化模拟...")
        print(f"纬度: {params['latitude']}°")
        print(f"摆动周期: {params['period']} 秒")
        print(f"自转周期: {params['rotation_period']} 秒")
        print(f"持续时间: {params['duration']} 秒")
        print(f"时间流速: {params['time_multiplier']}x")
        print(f"帧率: {params['fps']:.1f}")
        
        # 创建动画器实例
        animator = PendulumAnimator(**params)
        
        print("\n开始动画模拟...")
        print("关闭绘图窗口即可退出程序")
        print("\n提示: 要更改参数，请编辑 config.txt 文件后重新运行程序")
        
        # 创建并显示动画
        animation = animator.create_animation()
        plt.show()
        
    except KeyboardInterrupt:
        print("\n用户取消了模拟")
    except Exception as e:
        print(f"\n错误: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())