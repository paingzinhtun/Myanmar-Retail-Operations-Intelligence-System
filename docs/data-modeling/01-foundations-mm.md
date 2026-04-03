# 01 Foundations - Myanmar Version

## Data modeling ဆိုတာဘာလဲ

Data modeling ဆိုတာ real-world business မှာရှိတဲ့ အရာတွေ၊ ဖြစ်စဉ်တွေ၊ စည်းမျဉ်းတွေကို data structure အဖြစ် ဘယ်လို ကိုယ်စားပြုမလဲဆိုတာ ဆုံးဖြတ်တဲ့ process ပါ။

ကောင်းတဲ့ model တစ်ခုက table စုစည်းမှုသာမက reality ကို ရှင်းရှင်းလင်းလင်း ပြောပြနိုင်ရမယ်:

- ဘာတွေရှိလဲ
- ဘာတွေဖြစ်လဲ
- ဘာတွေချိတ်ဆက်နေသလဲ
- အချိန်နဲ့အမျှ ဘာတွေပြောင်းလဲနိုင်သလဲ

## အခြေခံ concept ၃ ခု

### 1. Entity

Entity ဆိုတာ အမှန်တကယ် ရှိနေတဲ့ thing တစ်ခုဖြစ်ပြီး identifier နဲ့ ခွဲခြားနိုင်ရတယ်။

ဥပမာ:

- customer
- product
- store
- supplier
- order

မေးသင့်တဲ့မေးခွန်း:

- ဒီအရာက သီးသန့် entity အနေနဲ့ ရှိသလား
- အချိန်ကြာကြာ repeatedly identify လုပ်ဖို့လိုသလား
- ဒီအရာကိုဖော်ပြဖို့ attributes တွေလိုသလား

### 2. Event

Event ဆိုတာ တစ်ချိန်ချိန်မှာ ဖြစ်ပျက်သွားတဲ့ business action တစ်ခုပါ။

ဥပမာ:

- order placed
- sale completed
- payment made
- stock replenished
- item returned

မေးသင့်တဲ့မေးခွန်း:

- တကယ်လို့ တစ်ခုခုဖြစ်သွားသလား
- ဘယ်အချိန်မှာ ဖြစ်သလဲ
- အဲဒီဖြစ်စဉ်က အကြိမ်ကြိမ် ဖြစ်နိုင်သလား
- measure လုပ်ချင်သလား

### 3. Relationship

Relationship ဆိုတာ entity တွေ event တွေကြားက ချိတ်ဆက်မှုပါ။

ဥပမာ:

- customer places orders
- order contains products
- store records sales
- supplier provides products

မေးသင့်တဲ့မေးခွန်း:

- ဘယ်အရာတွေချိတ်ဆက်နေသလဲ
- one-to-one, one-to-many, many-to-many ဘယ်အမျိုးအစားလဲ
- relationship ကိုယ်တိုင်မှာ attribute ထပ်လိုသလား

## Data က reality ကို ဘယ်လို ကိုယ်စားပြုလဲ

Business reality ကို အလွယ်ပြောရရင် layer ၃ ခုနဲ့ကြည့်လို့ရတယ်:

1. တည်ငြိမ်တဲ့ things
2. ဖြစ်ပျက်တဲ့ business actions
3. အပြန်အလှန် ချိတ်ဆက်ပေးတဲ့ rules

Retail system မှာ:

- product က stable thing
- customer က stable thing
- order placed က business action
- customer to order က relationship

ဒါကို model လုပ်ရင်:

```text
Customer -> Order -> Order Item -> Product
                  -> Payment
```

## ကောင်းတဲ့ model တစ်ခုရဲ့ လက္ခဏာ

ကောင်းတဲ့ data model တစ်ခုက:

- နားလည်ရလွယ်တယ်
- consistent ဖြစ်တယ်
- query လုပ်ရလွယ်တယ်
- နောက်တိုးချဲ့ရလွယ်တယ်
- business question တွေနဲ့ ကိုက်ညီတယ်

Weak model တွေမှာ များသောအားဖြင့်:

- meaning မတူတာတွေ table တစ်ခုထဲ ရောနေတယ်
- key မရှင်းဘူး
- logic တွေထပ်နေတယ်
- time behavior မရှင်းဘူး
- report တစ်ခုတည်းအတွက်ပဲ design လုပ်ထားတယ်

## အလေ့အကျင့်ကောင်း

Table တစ်ခုမဖန်တီးခင် ဒီမေးခွန်း ၅ ခုမေးပါ:

1. ဒါ entity လား event လား relationship လား
2. row တစ်ကြောင်းရဲ့ business meaning ကဘာလဲ
3. unique identifier ကဘာလဲ
4. ဘာတွေက အချိန်နဲ့အမျှ ပြောင်းမလဲ
5. နောက်ပိုင်း ဘယ် business question တွေဖြေဖို့လိုမလဲ

ဒီ habit ကိုရလာရင် modeling judgment က အများကြီးတက်လာမယ်။
