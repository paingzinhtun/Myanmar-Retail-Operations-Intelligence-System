# 05 Learning Roadmap - Myanmar Version

## သင်စတင်တဲ့နေရာ

ဟုတ်ပါတယ်။ ဒီ project က data modeling ကို in depth လေ့လာဖို့ အရမ်းကောင်းတဲ့ starting point ပါ။

ဘာလို့ကောင်းလဲဆိုတော့ ဒီ project မှာရှိပြီးသားအရာတွေက:

- raw business-like data
- cleaning pipeline
- dimension and fact modeling
- SQL analytics
- business questions နဲ့ တိုက်ရိုက်ချိတ်ထားတဲ့ model

Theory သီးသန့်လေ့လာတာထက် ဒီလို project-based learning က ပိုတန်ဖိုးရှိတယ်။

## Stage 1: Language ကိုအရင်သင်

အရင်ဆုံး ဒီ concepts တွေကိုတိတိကျကျ သိအောင်လုပ်ပါ:

- entity
- event
- relationship
- key
- fact table
- dimension table
- grain

Goal:

- ဒီ project ကိုသုံးပြီး term တစ်ခုချင်းစီကို ကိုယ့်စကားနဲ့ ပြန်ရှင်းနိုင်ရမယ်

Practice:

- `dim_product`, `dim_store`, `fact_sales` ကို အသံထွက်ရှင်းပြပါ
- `fact_sales` ရဲ့ grain ကို စာတစ်ကြောင်းနဲ့ရေးပါ

## Stage 2: Current model ကိုဖတ်တတ်အောင်လုပ်

ဒီ files တွေကို study လုပ်ပါ:

- [sql/schema.sql](c:\Users\HP\Desktop\Myn_retail\sql\schema.sql)
- [src/retail_intel/pipeline.py](c:\Users\HP\Desktop\Myn_retail\src\retail_intel\pipeline.py)
- [sql/metrics.sql](c:\Users\HP\Desktop\Myn_retail\sql\metrics.sql)

Goal:

- current model က retail analytics questions တွေကို ဘာကြောင့်ကောင်းကောင်းဖြေနိုင်လဲ နားလည်ရမယ်

Practice:

- raw row တစ်ကြောင်းကနေ cleaned data, fact table ထိ trace လုပ်ပါ
- `fact_sales` က `dim_product`, `dim_store` နဲ့ ဘယ်လိုချိတ်လဲ ပြန်ရှင်းပါ

## Stage 3: Tradeoff တွေကိုနားလည်

အခု deeper questions မေးပါ:

- `payment_type` ကို `fact_sales` ထဲထည့်ထားတာ ဘာကြောင့်လဲ
- supplier ကို `dim_product` ထဲထားတာ ဘာကြောင့်လဲ
- stock ကို movement events မဟုတ်ဘဲ value အနေနဲ့ထားတာ ဘာသဘောလဲ

Goal:

- model ဆိုတာ definition မဟုတ်ဘဲ design choice တွေရဲ့ စုပေါင်းဖြစ်တယ်ဆိုတာ နားလည်ရမယ်

Practice:

- current design ရဲ့ strengths ၃ ခုရေးပါ
- reality ပိုနက်လာရင် limitations ၃ ခုရေးပါ

## Stage 4: Model ကိုတိုးချဲ့

Future version ကို စပြီး sketch လုပ်ပါ:

- `dim_customer`
- `fact_order`
- `fact_order_item`
- `fact_payment`

Goal:

- business needs ကြီးလာသလို modeling ဘယ်လိုကြီးလာရမလဲ နားလည်ရမယ်

Practice:

- table အသစ်တိုင်းအတွက် grain ကို define လုပ်ပါ
- primary key နဲ့ foreign keys ကို စာရင်းရေးပါ
- table တစ်ခုချင်းစီက ဘယ် business questions တွေကို enable လုပ်မလဲ ပြောပါ

## Stage 5: Teach it

တကယ်နားလည်ချင်ရင် တခြားသူကိုပြန်သင်ကြားကြည့်ပါ။

ဒီ project ကိုသုံးပြီး ရှင်းပြနိုင်သင့်တာတွေ:

- data က reality ကို ဘယ်လိုကိုယ်စားပြုလဲ
- star schema ဘာကြောင့်အသုံးဝင်လဲ
- grain က report quality ကို ဘယ်လိုသက်ရောက်လဲ
- simple analytics model ကနေ richer retail model ကို ဘယ်လိုသွားမလဲ

Goal:

- beginner audience နဲ့ business audience နှစ်မျိုးလုံးအတွက် ပြန်ရှင်းနိုင်ရမယ်

## Sharing အတွက် teaching outline

ဒီ project ကို session ၅ ခုပြုလုပ်ပြီး သင်လို့ရတယ်:

1. Data modeling ဆိုတာဘာလဲ
2. Retail မှာ entities, events, relationships
3. ဒီ project က dimensions နဲ့ fact table ဘာကြောင့်သုံးလဲ
4. Grain ဆိုတာဘာလဲ၊ ဘာလို့အရေးကြီးလဲ
5. Model ကို future-proof ဘယ်လိုလုပ်မလဲ

## နောက်ထပ်လုပ်သင့်တဲ့ project tasks

Theory ကနေ practice ကိုသွားချင်ရင် ဒီ tasks တွေထဲက တစ်ခုခုလုပ်ပါ:

1. `dim_customer` table design ဆွဲပြီး entity ဖြစ်တာဘာကြောင့်လဲ ရှင်းပါ
2. `fact_order_item` schema draft ရေးပြီး grain define လုပ်ပါ
3. current model နဲ့ fuller order-based model ကို နှိုင်းယှဉ်တဲ့ document တစ်ခုရေးပါ
4. richer model design ကိုလိုအပ်တဲ့ SQL metric အသစ်တစ်ခုစဉ်းစားပါ

## Final advice

အစကတည်းက model ကို မလိုအပ်ဘဲ မရှုပ်စေပါနဲ့။

အရင်ဆုံး နားလည်အောင်လုပ်သင့်တာ:

- အခု reality ကိုဘယ်လို model လုပ်ထားလဲ
- current model က ဘာကြောင့်အလုပ်လုပ်လဲ
- reality ပိုနက်လာရင် ဘယ်နေရာမှာ break ဖြစ်မလဲ

ဒီ thinking က beginner level ကနေ strong modeling judgment ဆီကို ခေါ်သွားမယ်။
