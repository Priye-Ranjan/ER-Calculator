from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def home():
    return 'Hello World!!'

@app.get('/getAmountLumpsump')
async def getExpenseAmount(principal:float,ror:float,time:int,er:float)->float:
    netExpenseAmount =0
    finalAmount = principal
    for i in range(time):
        expenseAmount=((er/100)*finalAmount)
        finalAmount-=expenseAmount
        netExpenseAmount+=expenseAmount
        print(expenseAmount)
        # print(principal)
        SI=(finalAmount*ror)/100
        finalAmount+=SI
        
        return {'Expense Amount':netExpenseAmount,'Amount Invested':principal, 'Estimated Return':finalAmount-principal,'Total Value on closing MF':finalAmount-expenseAmount}

@app.get('/getAmountSIP')
async def getExpenseAmount(sip:float,ror:float,time:int,er:float)->float:
    netExpenseAmount =0
    sipAmount=0
    finalAmount = sip
    count=0
    for i in range(time*12):
        expenseAmount=((er/100)*finalAmount)
        finalAmount-=expenseAmount
        netExpenseAmount+=expenseAmount
        # print(netExpenseAmount)
        # print(principal)
        SI=(finalAmount*ror)/1200
        print(SI)
        finalAmount+=SI
        finalAmount+=sip
        sipAmount+=sip
        count+=1
    print(count)
    return {'Expense Amount':netExpenseAmount,'Amount Invested':sipAmount, 'Estimated Return':finalAmount,'Total Value on closing MF':finalAmount-expenseAmount}