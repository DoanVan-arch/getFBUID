import streamlit as st
import requests
import base64
import json
import pandas as pd

import re
def getUID(url):  
    headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
            "cache-control": "max-age=0",
            "cookie": "datr=nSR2Z_oJHz-4IM1RO18kh-7-; sb=nSR2Z3jWL2LzGxQFb8Hh5zmI; dpr=1.25; ps_l=1; ps_n=1; fr=0tNBmTCvSwJfOacCc..Bneanz..AAA.0.0.Bneaq3.AWWizVfr1ZQ; wd=816x703",
            "dpr": "1.25",
            "priority": "u=0, i",
            "sec-ch-prefers-color-scheme": "light",
            "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            "sec-ch-ua-full-version-list": '"Google Chrome";v="131.0.6778.205", "Chromium";v="131.0.6778.205", "Not_A Brand";v="24.0.0.0"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-model": "",
            "sec-ch-ua-platform": "Windows",
            "sec-ch-ua-platform-version": "8.0.0",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "viewport-width": "816"
        }
    # proxies = {
    #     "http": f"http://{proxy}",
    #     "https": f"http://{proxy}",
    # }
    response = requests.get(url,headers=headers)
    return response
def extract_post_ids(content):
    """
    Extract Facebook post IDs from a text file.

    Args:
        file_path (str): Path to the text file

    Returns:
        list: List of extracted post IDs
    """
    # Check if file exists
    

    # Define regex pattern to match "post_id":"NUMBERS"
    pattern = r'"post_id":"(\d+)"'

    # Find all matches
    matches = re.findall(pattern, content)

    # Print results
    if matches:
        print(f"Found {len(matches)} post IDs:")
        for i, post_id in enumerate(matches, 1):
            print(f"{i}. {post_id}")
    else:
        print("No post IDs found in the file.")

    return matches
def getcmt(id):
    url = "https://www.facebook.com/api/graphql/"

    headers = {
        "authority": "www.facebook.com",
        "method": "POST",
        "path": "/api/graphql/",
        "scheme": "https",
        "accept": "*/*",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
        "content-type": "application/x-www-form-urlencoded",
        "dpr": "1.25",
        "cookie": "dpr=1.25; sb=VEdzZ-YVx2zM4XwojJTWKbIc; datr=VEdzZyiQElyyh9HuzjaD5FQL; wd=816x722",
        "origin": "https://www.facebook.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "viewport-width": "982",
        "x-asbd-id": "129477",
        "x-fb-friendly-name": "CommentListComponentsRootQuery",
        "x-fb-lsd": "AVqpeqKFLLc",
    }

    data = {
        "av": "0",
        "__aaid": "0",
        "__user": "0",
        "__a": "1",
        "__req": "h",
        "dpr": "1",
        "__ccg": "GOOD",
        "__rev": "1019099659",
        "__s": "nvbf2u:n9bd15:vnouit",
        "__hsi": "7454361444484971104",
        "__dyn": "7xeUmwlEnwn8yEqxemh0no6u5U4e1Nxt3odEc8co2qwJyE24wJwpUe8hw2nVE4W0te1Rw8G11wBz83WwgEcEhwnU2lwv89k2C1Fwc60D85m1mzXw8W58jwGzE2ZwJK14xm3y1lU5O0Gpo8o1mpEbUGdwda3e0Lo4q58jwTwNwLwFg2Xwkoqwqo4eE7W1iwo8uwjUy2-2K0UE",
        "__csr": "glgLblEoxcJiT9dmdiqkBaFcCKmWEKHCJ4LryoG9KXx6V4VECaG4998yuimayo-49rDz4fyKcyEsxCFohheVoogOt1aVo-5-iVKAh4yV9bzEC4E8FaUcUSi4UgzEnw7Kw1Gp5xu7AQKQ0-o4N07QU2Lw0TDwfu04MU1Gaw4Cw6CxiewcG0jqE2IByE1WU0DK06f8F31E03jTwno1MS042pA2S0Zxaxu0B80x6awnEx0lU3AwzxG3u0Ro1YE1Eo-32ow34wCw9608vwVo19k059U0LR08MNu8kc05lCabxG0UUjBwaadBweq0y8kwdh0kS0gq2-0Dokw1Te0O9o1rsMS1GKl1MM0JSeCa014aw389o1pOwr8dU0Pu0Cix60gR04YweK1raqagS0UA08_o1bFjj0fS42weG0iC0dwwvUuyJ05pw4Goog1680iow2a8",
        "__comet_req": "15",
        "lsd": "AVqpeqKFLLc",
        "jazoest": "2929",
        "__spin_r": "1019099659",
        "__spin_b": "trunk",
        "__spin_t": "1735603773",
        "fb_api_caller_class": "RelayModern",
        "fb_api_req_friendly_name": "CommentListComponentsRootQuery",
        "variables": f'{{"commentsIntentToken":"RECENT_ACTIVITY_INTENT_V1","feedLocation":"PERMALINK","feedbackSource":2,"focusCommentID":null,"scale":1,"useDefaultActor":false,"id":"{id}","__relay_internal__pv__IsWorkUserrelayprovider":false}}',
        "server_timestamps": "true",
        "doc_id": "9051058151623566",
    }

    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except Exception as e:
        st.error(f"Error fetching comments: {str(e)}")
        return None

def extract_comments(response):
    comments = []

    try:
        edges = response['data']['node']['comment_rendering_instance_for_feed_location']['comments']['edges']

        for edge in edges:
            node = edge['node']
            cmt_id = node['id']
            message = node['preferred_body']['text'] if node.get('preferred_body') and node['preferred_body'].get('text') else 'Sticker or Media'
            author = node.get('author', {}).get('name', 'Unknown')
            timestamp = node.get('created_time', 'Unknown')

            comments.append({
                'Comment ID': cmt_id,
                'Author': author,
                'Message': message,
                'Timestamp': timestamp
            })

        return comments
    except Exception as e:
        st.error(f"Error extracting comments: {str(e)}")
        if response:
            st.error(f"Response structure: {json.dumps(response, indent=2)}")
        return []

# Streamlit UI
st.title("Facebook Comments Extractor")

# Input for post ID
post_id = st.text_input("Enter Facebook Post URL:", "https://www.facebook.com/watch?v=679649137799306")

if st.button("Fetch Comments"):
    if post_id:
        with st.spinner("Fetching comments..."):
            # Encode the post ID
            res =  getUID(post_id)
            post_id_list = extract_post_ids(res.text)
            post_id = post_id_list[0]
            encoded_id = base64.b64encode(f"feedback:{post_id}".encode('utf-8')).decode('utf-8')

            # Get comments
            response = getcmt(encoded_id)

            if response:
                comments = extract_comments(response)

                if comments:
                    # Display as table
                    st.subheader(f"Comments for Post ID: {post_id}")
                    df = pd.DataFrame(comments)
                    st.dataframe(df)

                    # Download option
                    csv = df.to_csv(index=False)
                    st.download_button(
                        label="Download Comments as CSV",
                        data=csv,
                        file_name=f"facebook_comments_{post_id}.csv",
                        mime="text/csv"
                    )
                else:
                    st.warning("No comments found or unable to extract comments.")
            else:
                st.error("Failed to fetch comments. Check the post ID and try again.")
    else:
        st.warning("Please enter a Facebook Post ID.")

# Add some helpful information
st.markdown("---")
st.markdown("""
### How to use:
1. Enter a Facebook post ID (the number in the post URL)
2. Click "Fetch Comments" to retrieve all comments
3. View the comments in the table
4. Download as CSV if needed
""")
