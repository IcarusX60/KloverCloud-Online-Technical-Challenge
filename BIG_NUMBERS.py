
def summation(n1,n2):

    if len(n1) > len(n2):
        temp = n1
        n1 = n2
        n2 = temp

    l1 = len(n1)
    l2 = len(n2)
    num1 = n1[::-1]
    num2 = n2[::-1]
    difference = l2 - l1
    result= ""


    carry = 0
    for i in range (l1):
        sum = int(num1[i]) + int(num2[i]) + carry
        result += str(sum % 10)
        carry = int(sum / 10)



    for i in range(l1,l2):
        sum = int(num2[i]) + carry
        result += str(sum % 10)
        carry = int(sum/10)

    if (carry):
        result += str(carry)
    
    result = result[::-1]
    return result



print(summation(input(),input()))