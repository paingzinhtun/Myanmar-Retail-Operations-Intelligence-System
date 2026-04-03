# 04 Future Proof Modeling - Myanmar Version

## Future-proof ဆိုတာဘာကိုဆိုလိုတာလဲ

Future-proof modeling ဆိုတာ အနာဂတ်ကို အကုန်ကြိုခန့်မှန်းဖို့ မဟုတ်ပါ။

Project ကိုနောက်ပိုင်းချဲ့လိုက်ရင် structure ကို အကုန်ပြန်ဖျက်ဆောက်စရာမလိုဘဲ grow လုပ်လို့ရအောင် design လုပ်ထားတာကို ဆိုလိုပါတယ်။

ဒီ retail project အတွက်ဆိုရင် current analytics model ကို အသုံးဝင်အောင်ထားပြီး business reality ပိုနက်လာတဲ့အခါ တဖြည်းဖြည်း တိုးချဲ့နိုင်ဖို့ပြင်ထားတာပါ။

## နောက်ထပ် တိုးလာနိုင်တဲ့ modeling areas

Project ကိုချဲ့မယ်ဆိုရင် အများဆုံးဖြစ်လာနိုင်တဲ့ additions တွေက:

- customer data
- order headers
- order line items
- payment events
- inventory movement events
- supplier dimension
- time dimension

## ပိုအားကောင်းတဲ့ future retail model

Practical target design တစ်ခုက:

```text
dim_customer
dim_product
dim_store
dim_supplier
dim_date

fact_order
fact_order_item
fact_payment
fact_inventory_movement
```

## ဘာလို့ concept တွေကို ခွဲထားသင့်လဲ

### Customer

`dim_customer` ထည့်လိုက်ရင် အောက်ကမေးခွန်းတွေဖြေနိုင်မယ်:

- ဘယ် customer က မကြာခဏ ဝယ်သလဲ
- repeat purchase behavior ဘယ်လိုလဲ
- customer lifetime value ဘယ်လောက်လဲ

### Order and order item

Order တစ်ခုထဲမှာ product အများကြီးပါနိုင်တဲ့အခါ order header နဲ့ order item ကို ခွဲရမယ်။

ဒါမှ:

- basket analysis
- true average order value
- multi-item promotions

လို metrics တွေဖြေနိုင်မယ်။

### Payment as its own event

Payment ကို separate event အဖြစ်ထားသင့်တဲ့ case တွေ:

- order တစ်ခုမှာ payment attempt အကြိမ်များနိုင်တယ်
- refund ဖြစ်နိုင်တယ်
- payment status ကို track လုပ်ချင်တယ်

### Inventory movement

`stock_on_hand` value ကအသုံးဝင်ပေမယ့် inventory movement events က ပိုနက်တယ်၊ ပိုယုံကြည်ရတယ်။

ဥပမာ:

- goods received
- transfer in
- transfer out
- adjustment
- sale deduction
- return to stock

Inventory က serious business function ဖြစ်လာတဲ့အခါ ဒီ model က အရမ်းအရေးကြီးလာမယ်။

## ရေရှည်ခံတဲ့ design principles

### Business meaning ကိုရှင်းအောင်ထား

Table တစ်ခုချင်းစီအတွက်:

- row တစ်ကြောင်းကဘာကိုဆိုလိုလဲ
- ဒီ table ဘာလို့ရှိတာလဲ

ဆိုတာ ရှင်းရမယ်။

### Analytics models မှာ stable surrogate keys ကိုပိုသုံး

ဥပမာ:

- `product_id`
- `store_id`
- `customer_id`

ဒီလို keys တွေက label ပြောင်းသွားရင်တောင် join မပျက်စေဘူး။

### Descriptive data နဲ့ event data ကို ခွဲထား

Product, store details အကုန်ကို event row တစ်ကြောင်းထဲ repeated ထည့်နေတာထက် dimension model က ပိုရှင်းတယ်။

### Time ကိုသေချာစဉ်းစား

Time က data systems ထဲမှာ အရမ်းအရေးကြီးတဲ့ growth area ပါ။

စဉ်းစားသင့်တာတွေ:

- event time
- load time
- update time
- business effective dates

### Change ကို မျှော်လင့်ထား

Reality က အမြဲပြောင်းတယ်:

- prices ပြောင်းနိုင်တယ်
- product names ပြောင်းနိုင်တယ်
- stores ပြောင်းရွှေ့နိုင်တယ်
- customers merge or split ဖြစ်နိုင်တယ်
- payments fail and retry ဖြစ်နိုင်တယ်

Model က reality ပိုရှုပ်လာလို့ မပျက်သင့်ဘူး။

## ဒီ project ကို ဘယ်လိုတိုးချဲ့သင့်လဲ

Realistic evolution path တစ်ခုက:

1. `dim_customer` ထည့်
2. simple sales rows ကို `fact_order` နဲ့ `fact_order_item` လို model ပြောင်း
3. `payment_type` ကို payment event model ထဲရွှေ့
4. supplier နဲ့ inventory movement tables ထည့်
5. reporting ပို advance ဖြစ်လာရင် time dimension ထည့်

ဒီလမ်းကြောင်းက current work ကိုမပျက်စေဘဲ model maturity ကို မြှင့်ပေးမယ်။

## အရေးကြီးဆုံး future-proof habit

Table တစ်ခုတည်ဆောက်မယ့်အချိန်တိုင်း implementation မလုပ်ခင် grain နဲ့ business definition ကို စာဖြင့်အရင်ရေးပါ။

ဒီ habit တစ်ခုတည်းက modeling mistake အများကြီးကို ကာကွယ်ပေးတယ်။
