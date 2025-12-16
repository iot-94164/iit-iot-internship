kg=lambda t:t*1000
g=lambda kg:kg*1000
mg=lambda g:g*1000
p=lambda mg:mg*0.0000022046

W=float(input("Enter weight in tonns :"))

print(f"ton to kg= {kg(W)}")
print(f"kg to g= {g(W)}")
print(f"g to mg= {mg(W)}")
print(f"mg to p= {p(W)}")