"""
You'll notice that in Problem 2, your monthly payment had to be a multiple of 
$10. Why did we make it that way? You can try running your code locally so 
that the payment can be any dollar and cent amount (in other words, the 
monthly payment is a multiple of $0.01). Does your code still work? It should, 
but you may notice that your code runs more slowly, especially in cases with 
very large balances and interest rates.

Well then, how can we calculate a more accurate fixed monthly payment than we 
did in Problem 2 without running into the problem of slow code? We can make 
this program run faster using a technique introduced in lecture - bisection 
search!

The following variables contain values as described below:
1. balance - the outstanding balance on the credit card
2. annualInterestRate - annual interest rate as a decimal

To recap the problem: we are searching for the smallest monthly payment such 
that we can pay off the entire balance within a year. What is a reasonable 
lower bound for this payment value? $0 is the obvious answer, but you can do 
better than that. If there was no interest, the debt can be paid off by 
monthly payments of one-twelfth of the original balance, so we must pay at 
least this much every month. One-twelfth of the original balance is a good 
lower bound.

What is a good upper bound? Imagine that instead of paying monthly, we paid 
off the entire balance at the end of the year. What we ultimately pay must be 
greater than what we would've paid in monthly installments, because the 
interest was compounded on the balance we didn't pay off each month. So a good 
upper bound for the monthly payment would be one-twelfth of the balance, after 
having its interest compounded monthly for an entire year.

In short:
Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

Write a program that uses these bounds and bisection search (for more info 
check out the Wikipedia page on bisection search) to find the smallest monthly 
payment to the cent (no more multiples of $10) such that we can pay off the 
debt within a year. Try it out with large inputs, and notice how fast it is 
(try the same large inputs in your solution to Problem 2 to compare!). Produce 
the same return value as you did in Problem 2.
"""

def lowest_payment(balance, annualInterestRate):
    monthly_int_rate = annualInterestRate / 12.0
    mp_lower_bound = balance / 12
    mp_upper_bound = (balance * (1 + monthly_int_rate)**12) / 12.0
    updated_bal = balance
    while abs(updated_bal) > 0.1:
        updated_bal = balance
        monthly_payment = round((mp_lower_bound + mp_upper_bound) / 2, 2)
        for m in range(12):
            monthly_unpaid_bal = updated_bal - monthly_payment
            updated_bal = monthly_unpaid_bal + monthly_int_rate * monthly_unpaid_bal
            updated_bal = round(updated_bal, 2)
        if updated_bal > 0:
            mp_lower_bound = monthly_payment
        else:
            mp_upper_bound = monthly_payment
    return round(monthly_payment, 2)

#print("Lowest Payment:", lowest_payment(balance, annualInterestRate))

# test
print("Lowest Payment:", lowest_payment(320000, 0.2))
print("Lowest Payment:", lowest_payment(999999, 0.18))
