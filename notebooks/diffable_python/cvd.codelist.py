# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# The following contains SnoMed / dm+dcodelists for medicines contained in chapter 2 of the [BNF - Cardiovascular System](https://openprescribing.net/bnf/02/). We may wish to further divide into various subsections for certain studies
#
# - 2.1: [Positive Inotropic Drugs](https://openprescribing.net/bnf/0201/)
# - 2.2: [Diuretics](https://openprescribing.net/bnf/0202/)
# - 2.3: [Anti-Arrhythmic Drugs](https://openprescribing.net/bnf/0203/)
# - 2.4: [Beta-Adrenoceptor Blocking Drugs](https://openprescribing.net/bnf/0204/)
# - 2.5: [Hypertension and Heart Failure](https://openprescribing.net/bnf/0205/)
# - 2.6: [Nit,Calc Block & Other Antianginal Drugs](https://openprescribing.net/bnf/0206/)
# - 2.7: [Sympathomimetics](https://openprescribing.net/bnf/0207/)
# - 2.8: [Anticoagulants And Protamine](https://openprescribing.net/bnf/0208/)
# - 2.9: [Antiplatelet Drugs](https://openprescribing.net/bnf/0209/)
# - 2.10:[Stable Angina, Acute/Crnry Synd&Fibrin](https://openprescribing.net/bnf/0210/)
# - 2.11:[Antifibrinolytic Drugs & Haemostatics](https://openprescribing.net/bnf/0211/)
# - 2.12:[Lipid-Regulating Drugs](https://openprescribing.net/bnf/0212/)
# - 2.13:[Local Sclerosants](https://openprescribing.net/bnf/0213/)

from ebmdatalab import bq
import os
import pandas as pd

# +
sql = '''WITH bnf_codes AS (
  SELECT bnf_code FROM hscic.presentation WHERE 
    bnf_code LIKE '02%' #BNF cvd chapter 
  
  )

SELECT "vmp" AS type, id, bnf_code, nm
FROM dmd.vmp
WHERE bnf_code IN (SELECT * FROM bnf_codes)

UNION ALL

SELECT "amp" AS type, id, bnf_code, descr
FROM dmd.amp
WHERE bnf_code IN (SELECT * FROM bnf_codes)

ORDER BY type, bnf_code, id'''

cvd_codelist = bq.cached_read(sql, csv_path=os.path.join('..','data','cvd_codelist.csv'))
pd.set_option('display.max_rows', None)
cvd_codelist
