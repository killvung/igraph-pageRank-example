
Calculating rank score of users on the Facebook group with igraph library

### HOW TO USE 
- Clone the repo 

- Run ```pip3 install -r requirements.txt``` to install the required modules (Actually only igraph in this case...)

- Run ```python3 graph-igraph-converter.py``` to see the example list.

#### Source dataset
`graph.json` is an example dataset I used as a source for this algorithm.

The format is:

```
{
    "user_id_01":[
        ["tagged_user_id_01"],
        ["tagged_user_id_02"],
        ...
        [tagged_user_id_n]
    ],
    "user_id_02":[
        ["tagged_user_id_01"],
        ["tagged_user_id_02"],
        ...
        [tagged_user_id_n]
    ],
    ...
    "user_id_n":[
        ["tagged_user_id_01"],
        ["tagged_user_id_02"],
        ...
        [tagged_user_id_n]
    ]
}
```

I put every `tagged_user` in a list, so that I may be able to include their other userful information (name, dob...) in the future
    
