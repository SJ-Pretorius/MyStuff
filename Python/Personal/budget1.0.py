while True:
    budget=4000
    absa_monthly=1000
    print()
    investec_available=input('Investec Available: R')
    if investec_available.isdigit()==True and int(investec_available)>=budget:
        investec_available=int(investec_available)
        while True:
            absa_available=input('Absa Available: R')
            if absa_available.isdigit()==True and int(absa_available)<=absa_monthly:
                absa_available=int(absa_available)
                transfer_absa=absa_monthly-absa_available
                transfer_savings=investec_available-transfer_absa-budget
                print()
                if transfer_savings>=0:
                    x=f'Transfer R{transfer_savings} to your savings account and R{transfer_absa} to your Absa account!'
                    print('-'*len(x))
                    print(x)
                    print('-'*len(x))
                    break
                else:
                    x=f'Transfer R{investec_available-budget} (and R{abs(transfer_savings)} from your savings account) to your Absa account!'
                    print('-'*len(x))
                    print(x)
                    print('-'*len(x))
                    print()
                    break
            else:
                print()
                print(f'Amount must be equal or less than R{absa_monthly}!')
                print()
                continue
    else:
        print()
        print(f'Amount must be equal or more than R{budget}!')
        continue