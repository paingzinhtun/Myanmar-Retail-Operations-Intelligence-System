# Data Modeling Learning Path - Myanmar Version

ဒီ folder က Myanmar Retail Operations Intelligence System project ကိုအခြေခံပြီး data modeling ကို လေ့လာဖို့နဲ့ တခြားသူတွေကိုလည်း ပြန်ရှင်းပြဖို့ ပြင်ဆင်ထားတဲ့ learning track ဖြစ်ပါတယ်။

ဒီ guide ရဲ့ ရည်ရွယ်ချက် ၂ ခုက:

- data modeling ကို အဆင့်လိုက် နားလည်အောင် လေ့လာရန်
- ဒီ project ကို ဥပမာယူပြီး meaningful အနေနဲ့ ပြန်မျှဝေနိုင်ရန်

## ဘာကြောင့် အရေးကြီးလဲ

Data modeling ဆိုတာ business reality ကို table, key, relationship, event အဖြစ် ပြောင်းပြီး သေချာတိကျ၊ ရေရှည်အသုံးဝင်တဲ့ data structure ဖြစ်အောင် ဒီဇိုင်းလုပ်တဲ့ အလုပ်ပါ။

ဒီ project မှာဆိုရင် retail လောကမှာ တကယ်ရှိတဲ့ product, store, sale တို့ကို analytics အတွက် သုံးလို့ကောင်းအောင် model လုပ်ထားတာပါ။

ဒီအပိုင်းကို ကောင်းကောင်းနားလည်လာရင်:

- SQL မရေးခင် table design ကို ပိုစဉ်းစားတတ်လာမယ်
- report တချို့ ဘာလို့ လွယ်ပြီး တချို့ ဘာလို့ ခက်သလဲ နားလည်လာမယ်
- project ကို နောက်ပိုင်း scale up လုပ်ရင် ပိုလွယ်လာမယ်
- data engineer, analytics engineer, BI developer တစ်ယောက်လို system ကို ပြန်ရှင်းပြနိုင်မယ်

## ဖတ်သင့်တဲ့ အစဉ်

1. [01-foundations-mm.md](c:\Users\HP\Desktop\Myn_retail\docs\data-modeling\01-foundations-mm.md)
2. [02-project-reality-map-mm.md](c:\Users\HP\Desktop\Myn_retail\docs\data-modeling\02-project-reality-map-mm.md)
3. [03-star-schema-and-grain-mm.md](c:\Users\HP\Desktop\Myn_retail\docs\data-modeling\03-star-schema-and-grain-mm.md)
4. [04-future-proof-modeling-mm.md](c:\Users\HP\Desktop\Myn_retail\docs\data-modeling\04-future-proof-modeling-mm.md)
5. [05-learning-roadmap-mm.md](c:\Users\HP\Desktop\Myn_retail\docs\data-modeling\05-learning-roadmap-mm.md)

## ဒီ folder ကို ဘယ်လိုသုံးမလဲ

- ကိုယ်တိုင်လေ့လာမယ်ဆိုရင် အစဉ်လိုက်ဖတ်ပါ
- sharing လုပ်မယ်ဆိုရင် topic တစ်ခုချင်းစီအလိုက် သီးသန့် file ကိုပေးလို့ရတယ်
- current schema နဲ့ future design ကို နှိုင်းယှဉ်ဖို့ examples တွေကို သုံးပါ
- project ကိုချဲ့မယ်ဆိုရင် roadmap file ကို ပြန်ကြည့်ပါ

## ဒီ project နဲ့ချိတ်ထားတဲ့ အဓိက files

- [sql/schema.sql](c:\Users\HP\Desktop\Myn_retail\sql\schema.sql)
- [src/retail_intel/pipeline.py](c:\Users\HP\Desktop\Myn_retail\src\retail_intel\pipeline.py)
- [src/retail_intel/data_generator.py](c:\Users\HP\Desktop\Myn_retail\src\retail_intel\data_generator.py)
- [sql/metrics.sql](c:\Users\HP\Desktop\Myn_retail\sql\metrics.sql)

## Big picture

Current project မှာ analytics အတွက်ကောင်းတဲ့ starting model တစ်ခုရှိပြီးသားပါ:

- `dim_product`
- `dim_store`
- `fact_sales`

ဒီ foundation က တော်တော်ကောင်းပါတယ်။

နောက်တစ်ဆင့် deeper learning က:

- reality ကို data အဖြစ် ဘယ်လိုကိုယ်စားပြုထားသလဲ
- ဘာတွေကို simplify လုပ်ထားသလဲ
- နောက်ပိုင်း grow လုပ်ရင် ဘာတွေထပ်တိုးလို့ရမလဲ

ဒီအပိုင်းကိုနားလည်လာတဲ့အချိန်မှာ data modeling ကို future-proof angle နဲ့ စဉ်းစားတတ်လာမယ်။
