# 03 Star Schema And Grain - Myanmar Version

## ဒီ project က star-style model ဘာလို့သုံးတာလဲ

Current design က analytics model ဖြစ်လို့ dimensions နဲ့ fact table pattern ကို သုံးထားတာပါ။

ဒီ pattern ကို star schema လို့ခေါ်ကြတယ်။

အလွယ်ပြောရရင်:

- dimensions က business entities ကိုဖော်ပြတယ်
- fact tables က measurable events ကိုမှတ်တမ်းတင်တယ်

ဒီ project မှာ:

- `dim_product` က dimension
- `dim_store` က dimension
- `fact_sales` က fact table

## Analytics အတွက် ဘာလို့ကောင်းလဲ

ဒီ structure ကြောင့် အောက်ကမေးခွန်းတွေကို လွယ်လွယ်ကူကူမေးနိုင်တယ်:

- revenue by day
- revenue by store
- revenue by product
- units sold by category
- stock risk by product and store

ဒါက [sql/metrics.sql](c:\Users\HP\Desktop\Myn_retail\sql\metrics.sql) ထဲက queries တွေ လုပ်နေတဲ့အရာပါပဲ။

## အရေးကြီးဆုံး concept: grain

Grain ဆိုတာ table တစ်ခုထဲက row တစ်ကြောင်းရဲ့ တိကျတဲ့ business meaning ဖြစ်တယ်။

Grain မရှင်းရင် model ကရှုပ်သွားပြီး metrics တွေ မယုံကြည်ရတော့ဘူး။

`fact_sales` ရဲ့ current grain ကို အနီးစပ်ဆုံး အခုလိုပြောလို့ရတယ်:

`store တစ်ခုမှာ date တစ်ခုအတွင်း product တစ်မျိုးအတွက် recorded sale row တစ်ကြောင်း`

ဒီ definition ကြောင့် table က product-level, store-level reporting ကို support လုပ်နိုင်တာပါ။

## Grain ဘာလို့အရေးကြီးလဲ

Grain က:

- ဘာ measure တွေ sum လုပ်လို့ရမလဲ
- joins ကို ဘယ်လို safe လုပ်မလဲ
- duplicate ဆိုတာဘာလဲ
- table က ဘာ question တွေဖြေနိုင်မလဲ

ဆိုတာကိုဆုံးဖြတ်ပေးတယ်။

Grain မတူတာတွေကို table တစ်ခုထဲရောလိုက်ရင် report တွေ မှားတတ်တယ်။

ဥပမာ:

- order-level fields နဲ့ item-level fields ကို rule မရှင်းဘဲ row တစ်ခုထဲထည့်တာ
- daily summary နဲ့ raw transaction ကို fact table တစ်ခုထဲရောတာ
- join လုပ်တဲ့အခါ fact duplication ဖြစ်သွားတာ

## Dimension table mindset

Dimension tables ထဲမှာ များသောအားဖြင့်:

- identifiers
- labels
- categories
- descriptive attributes

ပါမယ်။

ဒီ project မှာ:

- product name, category, supplier က descriptive fields
- store name, city, township က descriptive fields

ဒီ fields တွေက filtering, grouping, labeling အတွက် အသုံးဝင်တယ်။

## Fact table mindset

Fact tables ထဲမှာ များသောအားဖြင့်:

- foreign keys to dimensions
- dates or timestamps
- measurable numeric values

ပါမယ်။

ဒီ project မှာ:

- `product_id` နဲ့ `store_id` က dimension တွေဆီ join လုပ်ဖို့ keys
- `sale_date` က event ဖြစ်တဲ့အချိန်
- `quantity`, `unit_price`, `revenue` က measures

## အဓိက lesson

Analytics model design လုပ်တဲ့အခါ column ကနေမစဘဲ event နဲ့ grain ကနေစပါ။

ဒီမေးခွန်းစဉ်ကိုသုံးပါ:

1. ဘာ event ကို measure လုပ်နေလဲ
2. row တစ်ကြောင်းရဲ့ meaning ကဘာလဲ
3. ဒီ event ကို describe လုပ်မယ့် dimensions တွေဘာလဲ
4. measures တွေက အဲဒီ level နဲ့ကိုက်လား

ဒီလိုစဉ်းစားရင် model design က ပိုတည်ငြိမ်တယ်။
