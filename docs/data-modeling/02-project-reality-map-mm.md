# 02 Project Reality Map - Myanmar Version

## ဒီ project က ဘယ် reality ကို model လုပ်ထားတာလဲ

ဒီ project က full POS system မဟုတ်ဘဲ retail analytics scenario ကို model လုပ်ထားတာပါ။

Current schema ကို [sql/schema.sql](c:\Users\HP\Desktop\Myn_retail\sql\schema.sql) မှာကြည့်ရင်:

- `dim_product`
- `dim_store`
- `fact_sales`

ဒီသုံးခုကနေ project ကဘာကို focus လုပ်ထားလဲဆိုတာ ရှင်းသွားတယ်:

- ဘာ product တွေရှိလဲ
- ဘာ store တွေရှိလဲ
- ဘာ sales တွေဖြစ်ခဲ့လဲ

## Current entities

### Product

`dim_product` က product entity ကို ကိုယ်စားပြုတယ်။

ပါဝင်တဲ့ attributes:

- `product_id`
- `product_name`
- `category`
- `supplier`
- `default_unit_price`

Business meaning:

- product ဆိုတာ ရောင်းတဲ့ item
- category နဲ့ supplier က product ကိုဖော်ပြတဲ့ descriptive fields
- default unit price က reference value ဖြစ်ပြီး actual sale price နဲ့ အမြဲတူမနေပါ

### Store

`dim_store` က store entity ကို ကိုယ်စားပြုတယ်။

ပါဝင်တဲ့ attributes:

- `store_id`
- `store_name`
- `city`
- `township`

Business meaning:

- store ဆိုတာ sale ဖြစ်တဲ့နေရာ
- city နဲ့ township က location details

## Current event

### Sale

`fact_sales` က sales event ကို represent လုပ်တယ်။

ပါဝင်တဲ့ attributes:

- `sale_id`
- `sale_date`
- `product_id`
- `store_id`
- `quantity`
- `unit_price`
- `revenue`
- `stock_on_hand`
- `payment_type`

Business meaning:

- row တစ်ကြောင်းက date တစ်ခုမှာ store တစ်ခုအတွင်း product တစ်မျိုးရဲ့ recorded sale event တစ်ခုကို ဖော်ပြတယ်

ဒီ table က project ရဲ့ main measurable business activity ဖြစ်တယ်။

## Current relationships

Current model က ဒီ relationship တွေကို ဖော်ပြထားတယ်:

- product တစ်ခုက sales အများကြီးထဲမှာ ပါနိုင်တယ်
- store တစ်ခုက sales အများကြီးထဲမှာ ပါနိုင်တယ်
- sale တစ်ခုက product တစ်ခုနဲ့ ဆိုင်တယ်
- sale တစ်ခုက store တစ်ခုနဲ့ ဆိုင်တယ်

diagram အနေနဲ့:

```text
dim_product 1 -> many fact_sales
dim_store   1 -> many fact_sales
```

## Raw data က modeled data ဘယ်လိုဖြစ်လာလဲ

[src/retail_intel/data_generator.py](c:\Users\HP\Desktop\Myn_retail\src\retail_intel\data_generator.py) က product, store, quantity, price, stock, payment type ပါတဲ့ retail-like rows တွေ generate လုပ်တယ်။

[src/retail_intel/pipeline.py](c:\Users\HP\Desktop\Myn_retail\src\retail_intel\pipeline.py) ကတော့:

- values တွေကို clean လုပ်တယ်
- descriptive data ကို dimension table တွေခွဲတယ်
- measurable business activity ကို fact table ထဲ ထည့်တယ်

ဒီဟာက raw business record ကနေ analytics-friendly structure ကို ပြောင်းတဲ့ classic example ပါ။

## ဘာတွေ simplify လုပ်ထားလဲ

ဒီ project က intentional simplification ပါ။

အခုလောလောဆယ် မပါတာတွေက:

- customer
- order
- order item
- payment as separate table
- supplier as separate dimension
- inventory movement events

ဒါက current goal နဲ့ကိုက်ပါတယ်၊ ဘာလို့လဲဆိုတော့ project က full transaction processing system မဟုတ်ဘဲ analytics questions ဖြေဖို့ design လုပ်ထားတာကြောင့်ပါ။

## ဒါက impact ရှိသလား

ရှိပါတယ်။ တကယ် impact ရှိပါတယ်။

ဒီ project က data modeling အတွက် အရေးကြီးတဲ့ lesson တစ်ခုကို သင်ပေးတယ်:

- အစကတည်းက အကုန် model လုပ်ဖို့မလိုဘူး
- business question ဖြေဖို့ လုံလောက်အောင် reality ကို model လုပ်ရမယ်

ဒီ project က လက်ရှိမှာတင် အောက်ကမေးခွန်းတွေကို ဖြေနိုင်တယ်:

- ဘာတွေ ရောင်းခဲ့လဲ
- ဘယ် store မှာ ရောင်းခဲ့လဲ
- ဘယ် product က revenue များလဲ
- ဘယ်နေရာမှာ stock risk တက်လာလဲ

ဒီဟာက practical modeling value ပါ။
