
from pymongo import MongoClient
from pprint import pprint
import datetime
import json

def connection():
    # conexao ha base de dados
    client = MongoClient()
    client = MongoClient('mongodb+srv://root:root@cd.uxfsz.mongodb.net/test')
    db = client['banco']
    collection = db['banco']

    documents(collection)


def documents(col):
    arrid = []
    data = [{"document_name": "CardType", "card_type_designation": "mastercard", "created_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")},
            {"document_name": "Credit", "end_duration": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"), "initial_duration": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
             "amount": 10000000, "is_paid": True, "created_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"), "updated_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")},
            {"document_name": "AccountType", "account_type_designation": "debit",
            "created_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")},
            {"document_name": "File", "url": "www.docfake.com/cli/account",
            "created_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"), "updated_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")},
            {"document_name":"User","uuid_user":"251d251a6a","address":"Rua Sao Joao","city":"Lisboa","phone_number":963578694,"is_active":True,"first_name":"Paulo","last_name":"Jorge","cc_identification":"957427491az9","nif_identification":16513545641,"personal_email":"pauloj1990@gmail.com","dob":"1990-10-24","created_at":datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"),"updated_at":datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")},
            {"document_name":"User","uuid_user":"1613ad354","address":"Rua Olivais","city":"Lisboa","phone_number":924857545,"is_active":True,"first_name":"Joao","last_name":"Santos","cc_identification":"957427491az9","nif_identification":16513545641,"personal_email":"pauloj1990@gmail.com","dob":"1990-10-24","created_at":datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"),"updated_at":datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")},
            {"document_name":"OperationType","operation_name":"transaction","created_at":datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")},
            {"document_name":"CreditProcessStatus","status":"accepted","created_at":datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")},
             {"document_name":"Permission","permission_designation":"admin","created_at":datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"),"updated_at":datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")},           
            ]
    
    post_many_documents(data, col)
    arrid = get_id_from_data(data, arrid, col)
    data = [
            {"document_name":"Customer","id_user":arrid[4],"contract_number":924568634,"pin_code":6852,"created_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"),"updated_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")},
                            
            {"document_name":"Collaborator","id_user":arrid[5],"work_email_address":"joao.it@banco.com","work_phone_number":6852,"created_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"),"updated_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")},
             {"document_name": "Movement","start_balance":1600,"end_balance":1000,"reserved_balance":600,"id_operation_type": arrid[6] ,"uuid_movement":"242g4f5s3a54", "created_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")},
            ]

    post_many_documents(data, col)
    arrid = get_id_from_data(data, arrid, col)
    data = [{"document_name": "Account", "id_account_type": arrid[2], "created_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"),"updated_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"), "is_active": False, "balance": 1110.50, "files": [arrid[3]],"movements":[arrid[11]]}]

    post_many_documents(data, col)

    arrid = get_id_from_data(data, arrid, col)
    data = [{"document_name": "Card", "card_number": 123456789, "card_pin_number": 1234, "created_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"),"id_card_type":arrid[0],
             "update_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"), "valid_until": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"), "cvv": 711, "card_hoder_name": "joao", "is active": True, "id_account": arrid[12]},
            ]

    post_many_documents(data, col)
    arrid = get_id_from_data(data, arrid, col)
    data = [
     {"document_name": "Holder","id_account":arrid[12],"id_customer ":arrid[9],"is_active":True,"register_date":datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"), "created_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"),"updated_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")}    
            ]
    post_many_documents(data, col)
    arrid = get_id_from_data(data, arrid, col)
    data = [
     {"document_name": "HolderPermission","id_permission ":arrid[8],"id_holder":arrid[14],"is_permision_active":True, "created_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"),"updated_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")},    
          {"document_name":"CreditProcess","id_account":arrid[12],"id_customer":arrid[9],"id_collaborator":arrid[10],"credit_process_status":arrid[7],"credit":arrid[1],"status":"accepted","created_at":datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")}
          
            ]

    post_many_documents(data, col)
    get_collection(col)

def post_many_documents(post, col):
    col.insert_many(post)

def get_collection(col):
    cursor = list(col.find({}))
  
    for document in cursor:
        print(document)

def get_documents_id(document):
   
    return document["_id"]


def get_id_from_data(data, arrid, col):
    
    for tabela in range(len(data)):
       
        cursor = col.find({"document_name": data[tabela]["document_name"]})
        for document in cursor:
            
            if (get_documents_id(document) in arrid):
                continue
            else:
                arrid.append(get_documents_id(document))
    return arrid


print("Loading querys...")
connection()
# https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb
