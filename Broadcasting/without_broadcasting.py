"""
lets say we have an array(list) of elements which denote the list of items in a supermart
and let us try to update the price of everyitem by giving certain amount of discount without using numpy"""


item_price = [100,200,300]

new_price=[]


discount =10
for price in item_price:
    pricing = price - (price *(discount/100))
    new_price.append(pricing)

print(new_price)


"""
here, it works pretty fine, but the issue is looping, it works good for a small dataset, but not when we have large datasets , Then enters NUMPY -  it gives us the ability to perform same operations without iterative looping and thus its faster."""

