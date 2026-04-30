# Synapse Python Example

All 16 SDK endpoints with [pyrx-synapse](https://pypi.org/project/pyrx-synapse/).

## Setup

1. `python -m venv .venv && source .venv/bin/activate`
2. `pip install -r requirements.txt`
3. Copy `.env.example` to `.env`

## Examples

### Core
```bash
python track_event.py        # Track event
python track_batch.py        # Batch track
python identify_contact.py   # Identify contact
python identify_batch.py     # Batch identify
python send_email.py         # Send email
python async_example.py      # Async client
```

### Contacts
```bash
python contacts_list.py      python contacts_get.py
python contacts_update.py    python contacts_delete.py
```

### Templates
```bash
python templates_list.py     python templates_get.py
python templates_create.py   python templates_update.py
python templates_delete.py   python templates_preview.py
```

- [Synapse Docs](https://synapse.pyrx.tech/developers)
- [Python SDK](https://synapse.pyrx.tech/developers/sdks/python)
