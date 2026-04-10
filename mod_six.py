import threading
import time
import random

class MemoryObject:
    # Represents a single allocated object in memory.
    def __init__(self, obj_id):
        self.obj_id = obj_id
        self.marked = False

class MemoryManager:
    # Manages memory allocation and concurrent mark-and-sweep cleanup.
    def __init__(self, max_size):
        self.pool = {}          # The simulated heap: maps obj_id -> MemoryObject
        self.roots = {}         # Active references: maps thread_name -> list of obj_ids
        self.lock = threading.Lock() # Ensures thread-safe access to memory structures
        self.next_id = 0
        self.max_size = max_size

    def allocate(self, thread_name):
        # Simulates allocating an object in memory.
        with self.lock:
            if len(self.pool) >= self.max_size:
                print(f"[{thread_name}] ALLOCATION FAILED: Memory pool is full.")
                return None
            
            obj_id = self.next_id
            self.next_id += 1
            
            # Create object and add to memory pool
            self.pool[obj_id] = MemoryObject(obj_id)
            
            # Add to thread's root references simulating a variable holding the object
            if thread_name not in self.roots:
                self.roots[thread_name] = []
            self.roots[thread_name].append(obj_id)
            
            print(f"[{thread_name}] ALLOCATED: Object {obj_id}")
            return obj_id

    def release_reference(self, thread_name, obj_id):
        # Simulates an object going out of scope by removing its reference.
        with self.lock:
            if thread_name in self.roots and obj_id in self.roots[thread_name]:
                self.roots[thread_name].remove(obj_id)
                print(f"[{thread_name}] DROPPED REFERENCE: Object {obj_id} is now unreachable.")

    def mark_and_sweep(self):
        # Executes the Mark-and-Sweep garbage collection cycle.
        with self.lock:
            print("\n--- GC EVENT: Starting Mark-and-Sweep ---")
            
            # MARK PHASE: Traverse roots and mark reachable objects
            marked_count = 0
            for t_name, refs in self.roots.items():
                for obj_id in refs:
                    if obj_id in self.pool:
                        self.pool[obj_id].marked = True
                        marked_count += 1
            print(f"--- GC EVENT: Mark Phase Complete. {marked_count} objects marked reachable.")

            # SWEEP PHASE: Remove unmarked objects
            keys_to_delete = []
            for obj_id, obj in self.pool.items():
                if not obj.marked:
                    keys_to_delete.append(obj_id)
                else:
                    obj.marked = False # Reset mark for the next GC cycle

            for obj_id in keys_to_delete:
                del self.pool[obj_id]
                print(f"--- GC EVENT: RECLAIMED Object {obj_id}")

            print(f"--- GC EVENT: Sweep Phase Complete. {len(keys_to_delete)} objects reclaimed. ---\n")

def worker(manager, thread_name, iterations):
    # Simulates a thread doing work: allocating and releasing memory.
    for _ in range(iterations):
        # Request memory allocation
        obj_id = manager.allocate(thread_name)
        time.sleep(random.uniform(0.1, 0.3)) # Simulate processing time
        
        # Randomly drop the reference so it becomes garbage
        if obj_id is not None and random.choice([True, False]):
            manager.release_reference(thread_name, obj_id)
            
        time.sleep(random.uniform(0.1, 0.3))
    print(f"[{thread_name}] Finished execution.")

def garbage_collector(manager, duration):
    # Runs continuously in the background to clean up memory.
    start_time = time.time()
    while time.time() - start_time < duration:
        time.sleep(1.2) # Trigger GC every 1.2 seconds
        manager.mark_and_sweep()

if __name__ == "__main__":
    print("Initializing Concurrent Memory Manager Simulation\n")
    mem_manager = MemoryManager(max_size=20)

    # Define threads
    t1 = threading.Thread(target=worker, args=(mem_manager, "Thread-1", 5))
    t2 = threading.Thread(target=worker, args=(mem_manager, "Thread-2", 5))
    t3 = threading.Thread(target=worker, args=(mem_manager, "Thread-3", 5))
    gc_thread = threading.Thread(target=garbage_collector, args=(mem_manager, 6))

    # Start threads
    gc_thread.start()
    t1.start()
    t2.start()
    t3.start()

    # Wait for worker threads to finish
    t1.join()
    t2.join()
    t3.join()
    gc_thread.join()
    
    # Final cleanup to show empty heap after program exit
    mem_manager.roots.clear()
    mem_manager.mark_and_sweep()
    print("Simulation Complete.")