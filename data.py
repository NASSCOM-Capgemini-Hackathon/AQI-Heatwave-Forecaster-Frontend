# Libraries
import streamlit as st
import pandas as pd

# Data Sources
# @st.cache(ttl=1000, allow_output_mutation=True)
def get_data(query):
    if query == 'Transactions Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/579714e6-986e-421a-85dd-c32a8b41b25c/data/latest')

    elif query == 'Transactions Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4e0c69ff-9395-43c1-af49-f590f864d339/data/latest')

    elif query == 'Transactions Heatmap':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/9d8d54d4-b700-4d85-af17-8c29aa29d334/data/latest')

    elif query == 'New Users Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/d81c5861-0792-43ec-9f92-d89fbcf85e79/data/latest')
    
    elif query == 'Fee Payers':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/7eae69ea-2387-420d-b4b9-6eceeb5ef22d/data/latest')

    elif query == 'Swaps Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/b3d90320-3fcb-44f0-b0b9-3f72ee779dcb/data/latest')

    elif query == 'Swaps Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/fed187af-6c8e-49fc-82d1-1975926e3951/data/latest')


    elif query == 'Swaps Heatmap':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3fa50926-77bc-44f8-b190-7bd48d408c85/data/latest')

    elif query == 'Swaps DEXs Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/9e0dace3-69d7-44fb-810c-e3b819b2b8de/data/latest')

    elif query == 'Swaps DEXs Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/5563d79a-a937-4e04-a74e-b75f284c57cb/data/latest')
        
    elif query == 'Transfers Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/41eb418f-d231-4a1f-a1c8-e7cc0ff2fddb/data/latest')

    elif query == 'Transfers Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/76276234-81ba-44fd-8341-7cde62d30abc/data/latest')

    elif query == 'Transfers Heatmap':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/933b930f-b611-469e-9e03-b0d5c5b0242b/data/latest')

    elif query == 'Transfers Distribution':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a17c8548-2834-4600-bc78-a0efb6d12de4/data/latest')

    elif query == 'Transfers Transferring Users':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/2f9e94d0-79b9-49a5-be9a-eb289e9890d4/data/latest')

    elif query == 'Transfers Wallet Types':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/cc07b022-fd08-459f-a9a3-cf8082221414/data/latest')

    elif query == 'Swaps Types Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/770cc6a0-bc32-49fb-942b-84c82da5a533/data/latest')

    elif query == 'Swaps Types Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3ec65249-62fe-49e6-bf85-513af7896e34/data/latest')

    elif query == 'Swaps Assets Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/060d6f19-6e02-4be3-b262-05a91e694986/data/latest')

    elif query == 'Swaps Assets Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/0139649d-6c38-4ee6-9e20-fff34e452fe6/data/latest')
        
    elif query == 'NFTs Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a9dee9b9-bfd8-4fed-b49b-a03767306d89/data/latest')

    elif query == 'NFTs Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/6ec4aca1-3d25-4233-bec2-0443b27d3e6c/data/latest')

    elif query == 'NFTs Heatmap':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/62fa2182-ca1b-4648-a363-8d1ce591253e/data/latest')

    elif query == 'NFTs Marketplaces Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8f4e8520-52af-4d57-b29e-e513f62f8fa9/data/latest')

    elif query == 'NFTs Marketplaces Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8fcca211-4bc6-444d-8696-0a583e2966a6/data/latest')

    elif query == 'NFTs Collections Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/eaa5902c-0206-4fd7-8eb4-b15ecf9a71b4/data/latest')

    elif query == 'NFTs Collections Daily':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/3cb9e6f6-849b-47e6-8c7e-b454e1394d6b/data/latest')

    return None