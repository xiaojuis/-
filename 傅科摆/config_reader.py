"""
配置文件读取模块
"""
import re
from constants import (
    DEFAULT_LATITUDE, DEFAULT_PERIOD, DEFAULT_AMPLITUDE,
    DEFAULT_DURATION, DEFAULT_FPS, DEFAULT_ROTATION_PERIOD
)

def parse_config_line(line):
    """解析配置文件中的单行内容。
    
    Args:
        line (str): 配置文件中的一行
        
    Returns:
        tuple: (参数名, 参数值) 或 None（如果是注释或空行）
    """
    # 移除注释
    line = line.split('#')[0].strip()
    if not line:
        return None
        
    # 查找参数名和值
    match = re.match(r'(\w+)\s*=\s*([-+]?\d*\.?\d+)', line)
    if match:
        return match.group(1), float(match.group(2))
    return None

def validate_parameter(name, value, min_value=None, max_value=None):
    """验证参数值是否在有效范围内。
    
    Args:
        name (str): 参数名
        value (float): 参数值
        min_value (float, optional): 最小允许值
        max_value (float, optional): 最大允许值
        
    Returns:
        float: 有效的参数值
    
    Raises:
        ValueError: 如果参数值无效
    """
    if min_value is not None and value < min_value:
        raise ValueError(f"{name} 必须大于 {min_value}")
    if max_value is not None and value > max_value:
        raise ValueError(f"{name} 必须小于 {max_value}")
    return value

def read_simulation_parameters(config_file='config.txt'):
    """从配置文件读取模拟参数。
    
    Args:
        config_file (str): 配置文件路径
        
    Returns:
        dict: 模拟参数字典
    """
    # 默认参数
    params = {
        'latitude': DEFAULT_LATITUDE,
        'period': DEFAULT_PERIOD,
        'amplitude': DEFAULT_AMPLITUDE,
        'duration': DEFAULT_DURATION,
        'fps': DEFAULT_FPS,
        'rotation_period': DEFAULT_ROTATION_PERIOD,
        'time_multiplier': 1.0
    }
    
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            for line in f:
                result = parse_config_line(line)
                if result:
                    name, value = result
                    if name in params:
                        params[name] = value
        
        # 验证参数
        params['latitude'] = validate_parameter('纬度', params['latitude'], -90, 90)
        params['period'] = validate_parameter('摆动周期', params['period'], 0.1)
        params['rotation_period'] = validate_parameter('天体自转周期', params['rotation_period'], 1)
        params['duration'] = validate_parameter('模拟持续时间', params['duration'], 1)
        params['time_multiplier'] = validate_parameter('时间流速倍率', params['time_multiplier'], 0.1)
        
    except FileNotFoundError:
        print(f"警告: 未找到配置文件 {config_file}，使用默认参数")
    except ValueError as e:
        print(f"警告: 配置文件中的参数无效 - {str(e)}，使用默认值")
    
    return params