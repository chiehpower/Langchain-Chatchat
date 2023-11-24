import requests
import json

data = {
    "query": "BLOPRESS, 8, Candesartan cilexetil Tablets, 8mg, 28 Tablets, HEALTHCARE, CELLTRION",
    "knowledge_base_name": "samples",
    "top_k": 1,
    "score_threshold": 1,
    "stream": True,
    "model_name": "chatglm-6b",
    "temperature": 0.7,
    "local_doc_url": False
}


server_url = "http://0.0.0.0:7861"

response = requests.post(f"{server_url}/chat/knowledge_base_chat", json=data, stream=True)

if response.status_code == 200:
    response_data = json.loads(response.text)

    docs = response_data.get("docs", [])
    # print(docs)
    if docs:
        res = docs[0].split('_key:')[1]
        # print(res)
        res = res.split('\nMedicine name: ')
        key = int(res[0].strip())
        print(key)

        res = res[1].split('\nDrug Label:')
        Medicine_name = res[0]
        print(Medicine_name)
        # doc_url = docs[0].split("] ")[-1].strip()
        # print("Document URL:", doc_url)
    else:
        print("No documents found in the response.")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
