def arithmetic_arranger(problems, opt1 = None):

  def errorFinder(problems):
    #Error 1
    if len(problems) > 5:
      return "Error: Too many problems."
    #Error 2 
    for equation in problems:
      equation = equation.split()
      if equation[1] == '+' or equation[1] == '-':
        #Error 3
        try:
          num1 = int(equation[0])
          num2 = int(equation[2])
        except:
          return "Error: Numbers must only contain digits."
        #Error 4
        if (len(str(num1)) > 4 or len(str(num2)) > 4):
          return "Error: Numbers cannot be more than four digits."
      else:
        return "Error: Operator must be '+' or '-'."
        
    return "No problems"
  if errorFinder(problems) != "No problems":
    return errorFinder(problems)
  
  def solve(num1, oper, num2):
    if oper == '+':
      return int(num1) + int(num2)
    elif oper == '-':
      return int(num1) - int(num2)

     
  indent = 0
  dash = ''
  ans = ''
  top = ''
  bottom = ''

  for equation in problems:
    equation = equation.split()

    if len(equation[0]) >= len(equation[2]):
      indent = len(equation[0]) - len(equation[2])
      dashlen = len(equation[0]) + 2

      top = top + "  " + equation[0] + "    "
      bottom = bottom + equation[1] + " "

      while indent > 0:
        bottom = bottom + " "
        indent = indent - 1

      bottom = bottom + equation[2] + "    "

      while dashlen > 0:
        dash = dash + "-"
        dashlen = dashlen - 1
      
      dash = dash + "    "

      answer = solve(equation[0], equation[1], equation[2])
      ansIndent = len(equation[0]) + 2 - len(str(answer))

      while ansIndent > 0:
        ans = ans + " "
        ansIndent = ansIndent - 1

      ans = ans + str(answer) + "    "

    elif len(equation[2]) > len(equation[0]):
      indent = (len(equation[2]) - len(equation[0])) + 2
      dashlen = len(equation[2]) + 2

      while indent > 0:
        top = top + ' '
        indent = indent - 1

      top = top + equation[0] + "    "
      bottom = bottom + equation[1] + " " + equation[2] + "    "

      while dashlen > 0:
        dash = dash + "-"
        dashlen = dashlen - 1

      dash = dash + "    "

      answer = solve(equation[0], equation[1], equation[2])
      ansIndent = len(equation[2]) + 2 - len(str(answer))

      while ansIndent > 0:
        ans = ans + " "
        ansIndent = ansIndent - 1

      ans = ans + str(answer) + "    "

  if opt1 == True:
    return top.rstrip() + "\n" + bottom.rstrip() + "\n" + dash.rstrip() + "\n" + ans.rstrip()

  return top.rstrip() + "\n" + bottom.rstrip() + "\n" + dash.rstrip()
