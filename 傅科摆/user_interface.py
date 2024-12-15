"""
傅科摆模拟程序的用户界面模块
"""
import sys
from constants import (
    DEFAULT_LATITUDE, DEFAULT_PERIOD, DEFAULT_AMPLITUDE,
    DEFAULT_DURATION, DEFAULT_FPS, DEFAULT_ROTATION_PERIOD
)

def get_float_input(prompt, default_value, min_value=None, max_value=None):
    """获取用户输入的浮点数，并进行验证。
    
    参数:
        prompt (str): 输入提示信息
        default_value (float): 默认值
        min_value (float, optional): 最小允许值
        max_value (float, optional): 最大允许值
        
    返回:
        float: 有效的输入值
    """
    while True:
        try:
            user_input = input(f"{prompt} [{default_value}]: ").strip()
            if not user_input:
                return default_value
            
            value = float(user_input)
            
            if min_value is not None and value < min_value:
                print(f"输入值必须大于 {min_value}")
                continue
            if max_value is not None and value > max_value:
                print(f"输入值必须小于 {max_value}")
                continue
                
            return value
        except ValueError:
            print("请输入有效的数字")

def get_simulation_parameters():
    """获取用户输入的模拟参数。
    
    返回:
        dict: 模拟参数字典
    """
    print("\n=== 傅科摆模拟参数设置 ===\n")
    
    # 获取纬度
    latitude = get_float_input(
        "请输入纬度（度）（90° = 北极，-90° = 南极）",
        DEFAULT_LATITUDE,
        min_value=-90,
        max_value=90
    )
    
    # 获取摆动周期
    period = get_float_input(
        "请输入摆动周期（秒）",
        DEFAULT_PERIOD,
        min_value=0.1
    )
    
    # 获取天体自转周期
    rotation_period = get_float_input(
        "请输入天体自转周期（秒）（地球 = 86400）",
        DEFAULT_ROTATION_PERIOD,
        min_value=1
    )
    
    # 获取模拟持续时间
    duration = get_float_input(
        "请输入模拟持续时间（秒）",
        DEFAULT_DURATION,
        min_value=1
    )
    
    # 获取时间流速倍率
    time_multiplier = get_float_input(
        "请输入时间流速倍率（1 = 实时，>1 = 加速，<1 = 减速）",
        1.0,
        min_value=0.1
    )
    
    return {
        'latitude': latitude,
        'period': period,
        'amplitude': DEFAULT_AMPLITUDE,
        'duration': duration,
        'fps': DEFAULT_FPS,  # 保持恒定帧率
        'rotation_period': rotation_period,
        'time_multiplier': time_multiplier
    }