def oturikeisan(goods,pay):
    coins = [500,100,50,10]
    goods = int(goods)
    pay = int(pay)
    sub = pay - goods
    result = {}

    if sub < 0:
        return "支払いが不足しています"

    for coin in coins:
        count = sub // coin
        if count > 0:
            result[coin] = count
            sub -= coin * count
    if sub > 0:
        result["残り"] = sub
    return result



goods = input("購入する商品の金額")
pay = input("お支払する金額を入力してください")
change_result = oturikeisan(goods,pay)
print(f"お釣りの枚数:{change_result}")