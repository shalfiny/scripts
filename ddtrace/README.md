# Usage

1. Find the /api/v1/trace/ response in the DD network tab
2. Save `spans` as a file
3. Run: `./nesttrace.py [file name] [root_id]` to print the trace as a tree. You can replace `root_id` with any node id to focuse on a specific area
4. Run: `./tracedetails.py [file_name] [id]` to print all the details of a specific span

Example[s]:
1. `./nesttrace.py example.json 1`

Output:
```
5sec span 1: get [1]
 2sec span 2: request #1 [2]
 3sec span 3: request #2 [3]
```

2. `./tracedetails.py example.json 2`

Output:
```json
{
  "name": "span 2",
  "duration": 2,
  "resource": "request #1",
  "children_ids": []
}
```