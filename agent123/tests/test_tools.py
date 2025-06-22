import pytest
import sys
import os

# Add the src directory to PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from agent123.tools.custom_tool import MyCustomTool, MyCustomToolInput

def test_custom_tool_initialization():
    """
    Test that MyCustomTool can be instantiated.
    """
    tool = MyCustomTool()
    assert isinstance(tool, MyCustomTool)
    assert tool.name == "Name of my tool"
    assert hasattr(tool, 'description')
    assert hasattr(tool, 'args_schema')

def test_custom_tool_execution():
    """
    Test the execution functionality of MyCustomTool.
    """
    tool = MyCustomTool()
    input_data = MyCustomToolInput(argument="test")
    result = tool._run(input_data.argument)
    assert isinstance(result, str)
    assert result == "this is an example of a tool output, ignore it and move along."
    
    # Test with invalid input - should not raise an error since the tool doesn't handle it
    invalid_result = tool._run(None)
    assert isinstance(invalid_result, str)
    assert invalid_result == "this is an example of a tool output, ignore it and move along."

def test_custom_tool_validation():
    """
    Test input validation for MyCustomTool.
    """
    tool = MyCustomTool()
    input_data = MyCustomToolInput(argument="test")
    assert isinstance(input_data, MyCustomToolInput)
    
    # Test validation with invalid input
    with pytest.raises(ValueError):
        MyCustomToolInput(argument=None)
