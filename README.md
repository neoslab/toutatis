# Toutatis

This script retrieves detailed information about an Instagram user using the Instagram API. The script requires an Instagram session ID and a username to fetch and display various user details, including profile information, linked Facebook account details, and more.

## Features

- Fetch basic Instagram user information such as username, user ID, full name, and more.
- Retrieve and display follower count, following count, and media count.
- Obtain profile picture URL and biography.
- Fetch linked Facebook account details, if available.
- Retrieve obfuscated email and phone number, if available.
- Handles rate limits and user not found errors gracefully.

## Requirements

- Python 3.6 or higher
- Required Python libraries: `argparse`, `requests`, `phonenumbers`, `pycountry`

* * *

## Installation

**Clone the repository**

```bash
git clone https://github.com/neoslab/toutatis
```

**Change to the project directory**

```bash
cd toutatis
```

**Install the required libraries**

```bash
python -m pip install -r requirements.txt
```

* * *

## Usage

To run the script, use the following command:

```bash
python toutatis.py -s <SESSIONID> -u <USERNAME>
```

### Arguments

- `-s`, `--sessionid` (required): Your Instagram session ID.
- `-u`, `--username` (required): The username of the Instagram user you want to fetch information for.

### Example

```bash
python toutatis.py -s YOUR_SESSION_ID -u target_username
```

### Output

The script outputs detailed information about the specified Instagram user, including:

- Username
- User ID
- Full name
- Verified status
- Business account status
- Private account status
- Category
- Daily limit
- API enabled status
- Followers count
- Following count
- Posts count
- Fan club details
- External URL
- IGTV posts count
- WhatsApp linked status
- Memorial status
- New IG user status
- Parent control status
- Quiet mode status
- Biography
- Anonymous profile picture status
- Guide status
- Highlight reels status
- IG profile status
- Music profile status
- Placed orders status
- Private collections status
- Saved items status
- Video features status
- Creator agent status
- Hiding comment status
- Hiding stories status
- Profile picture URL
- Linked Facebook user ID, name, and account creation time (if available)
- Public email (if available)
- Public phone number (if available)
- Obfuscated email and phone number (if available)

### Error Handling

The script handles the following errors:

- User not found
- Rate limit exceeded

* * *

### Acknowledgements

This script is based on `[https://github.com/megadose/toutatis](https://github.com/megadose/toutatis)`.