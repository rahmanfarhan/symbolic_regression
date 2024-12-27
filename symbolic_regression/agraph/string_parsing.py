

def infix_to_postfix(infix_tokens):
    """Converts a list of infix tokens into its corresponding
    list of postfix tokens (e.g. ["a", "+", "b"] -> ["a", "b", "+"])

    Based on the Dijkstra's Shunting-yard algorithm

    Parameters
    ----------
    infix_tokens : list of str
        A list of infix string tokens

    Returns
    -------
    postfix_tokens : list of str
        A list of postfix string tokens corresponding
        to the expression given by infix_tokens
    """
    stack = []  # index -1 = top (the data structure, not a command array)
    output = []
    for token in infix_tokens:
        if token in operators:
            while len(stack) > 0 and stack[-1] in operators and \
                (precedence[stack[-1]] > precedence[token] or
                 precedence[stack[-1]] == precedence[token] and token != "^"):
                output.append(stack.pop())
            stack.append(token)
        elif token == "(" or token in functions:
            stack.append(token)
        elif token == ")":
            while len(stack) > 0 and stack[-1] != "(":
                output.append(stack.pop())
            if len(stack) == 0 or stack.pop() != "(":  # get rid of "("
                raise RuntimeError("Mismatched parenthesis")
            if len(stack) > 0 and stack[-1] in functions:
                output.append(stack.pop())
        else:
            output.append(token)

    while len(stack) > 0:
        token = stack.pop()
        if token == "(":
            raise RuntimeError("Mismatched parenthesis")
        output.append(token)

    return output



def eq_string_to_infix_tokens(eq_string):
    """Converts an equation string to infix_tokens

    Parameters
    ----------
    eq_string : str
        A string corresponding to an equation

    Returns
    -------
    infix_tokens : list of str
        A list of string tokens that correspond
        to the expression given by eq_string
    """
    if any(bad_token in eq_string for bad_token in ["zoo", "I", "oo",
                                                       "nan"]):
        raise RuntimeError("Cannot parse inf/complex")
    eq_string = eq_string.replace(")(", ")*(").replace("**", "^")

    eq_string = negative_pattern.sub(r"-1 * \1", eq_string)
    # replace -token with -1.0 * token if token != a number

    tokens = non_unary_op_pattern.sub(r" \1 ", eq_string).split(" ")
    tokens = [x.lower() for x in tokens if x != ""]
    return tokens


def eq_string_to_command_array_and_constants(eq_string):
    """Converts an equation string to its corresponding command
    array and list of constants

    Parameters
    ----------
    eq_string : str
        A string corresponding to an equation

    Returns
    -------
    command_array, constants : Nx3 numpy array of int, list of numeric
        A command array and list of constants
        corresponding to the expression given by eq_string
    """
    infix_tokens = eq_string_to_infix_tokens(eq_string)
    postfix_tokens = infix_to_postfix(infix_tokens)
    return postfix_to_command_array_and_constants(postfix_tokens)
