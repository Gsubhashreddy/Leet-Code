class Node{
    int val;
    Node prev;
    Node next;
    int key;
    
    public Node(int key, int val){
        this.key = key;
        this.val = val;
    }
}

class LRUCache {
    Node head;
    Node tail;
    HashMap<Integer, Node> a;
    int capacity;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.head = new Node(-1, -1);
        this.tail = new Node(-1,-1);
        a = new HashMap<>();
         head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        if (!a.containsKey(key)) {
            return -1;
        }

        Node node = a.get(key);
        removeNode(node);
        add(node);
        return node.val;
    }
    
   public void add(Node node) {
        Node previousEnd = tail.prev;
        previousEnd.next = node;
        node.prev = previousEnd;
        node.next = tail;
        tail.prev = node;
    }
    public void removeNode(Node node){
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
    
    public void put(int key, int value) {
        if(this.a.containsKey(key)){
            Node tmp = this.a.get(key);
            removeNode(tmp);
            // this.a.remove(key);
        }
        Node newNode = new Node(key,value);
        this.a.put(key,newNode);
        add(newNode);
        if(this.a.size() > capacity){
            Node nodeToDelete = head.next;
            removeNode(nodeToDelete);
            this.a.remove(nodeToDelete.key);
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */