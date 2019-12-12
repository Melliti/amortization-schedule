from amortization.amount import calculate_amortization_amount
from amortization.schedule import amortization_schedule
from tabulate import tabulate

class amortizationSchedule:
    def makeSchedule(self, p, r, n):
        table = (x for x in amortization_schedule(int(p), (int(r)/12)/100, int(n)))
        print(
            tabulate(
                table,
                headers=["Number", "Amount", "Interest", "Principal", "Balance"],
                floatfmt=",.2f",
                numalign="right"
            )
        )
