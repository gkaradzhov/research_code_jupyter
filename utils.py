import csv 


def load_csv(filepath):
   result = []
   with open(filepath, 'r', encoding='utf8') as rf:
      csv_reader = csv.reader(rf)
      for item in csv_reader:
         result.append(item)

   return result			


