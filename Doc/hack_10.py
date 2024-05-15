"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    transformed_result = []
    for char in result:
        if char == "o":
            transformed_result.append("0")
        elif char == "i":
            transformed_result.append("1")
        elif char == "a":
            transformed_result.append("@")
        else:
            transformed_result.append(char.upper())
    return transformed_result  