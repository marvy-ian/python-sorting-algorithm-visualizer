import os
import sys
import time
import random

if os.name == 'nt':
    os.system('')

RESET = "\033[0m"
WHITE = "\033[97m"
YELLOW = "\033[93m"  
GREEN = "\033[92m"   
CYAN = "\033[96m"    
BOLD = "\033[1m"

class Stats:
    def __init__(self):
        self.steps = 0
        self.swaps = 0
        self.comparisons = 0
        self.start_time = 0.0
        self.elapsed_ms = 0.0

current_stats = Stats()
delay_time = 0.1  


def clear_screen():
    sys.stdout.write("\033[H\033[2J")
    sys.stdout.flush()

def draw_frame(array, algo_name, active_indices=None, sorted_indices=None):
    if active_indices == None: active_indices = []
    if sorted_indices == None: sorted_indices = []
    
    clear_screen()
    n = len(array)
    
    print(f"{BOLD}{CYAN}=== SORTING VISUALIZER ==={RESET}")
    print(f"{BOLD}Algorithm:{RESET} {algo_name} | {BOLD}Array Size (N):{RESET} {n}")
    print("-" * 50)
    
    print(f"{BOLD}Steps:{RESET} {current_stats.steps:<6} | "
          f"{BOLD}Comparisons:{RESET} {current_stats.comparisons:<6} | "
          f"{BOLD}Swaps:{RESET} {current_stats.swaps:<6}")
    print("-" * 50)
    
    max_val = max(array) if array else 1
    for i, val in enumerate(array):
        bar_length = int((val / max_val) * 30) if max_val > 0 else 0
        bar = "█" * bar_length
        
        if i in active_indices:
            color = YELLOW
        elif i in sorted_indices:
            color = GREEN
        else:
            color = WHITE
            
        print(f"{i:2d} [{val:3d}] : {color}{bar}{RESET}")
        
    print("-" * 50)
    
    progress = int((current_stats.steps % 20) + 1)
    prog_bar = "■" * progress + " " * (20 - progress)
    print(f"{CYAN}Progress: [{prog_bar}]{RESET}")
    
    sys.stdout.flush()
    time.sleep(delay_time)


def recursive_bubble_sort(arr, n):
    if n <= 1:
        return
    
    def bubble_pass(i):
        if i >= n - 1:
            return
        current_stats.comparisons += 1
        current_stats.steps += 1
        
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            current_stats.swaps += 1
            draw_frame(arr, "Bubble Sort (Recursive)", active_indices=[i, i+1])
        else:
            draw_frame(arr, "Bubble Sort (Recursive)", active_indices=[i, i+1])
            
        bubble_pass(i + 1)

    bubble_pass(0)
    recursive_bubble_sort(arr, n - 1)


def recursive_insertion_sort(arr, n):
    if n <= 1:
        return
    
    recursive_insertion_sort(arr, n - 1)
    last = arr[n - 1]
    
    def insert_element(i):
        current_stats.steps += 1
        if i >= 0:
            current_stats.comparisons += 1
            if arr[i] > last:
                arr[i + 1] = arr[i]
                current_stats.swaps += 1
                draw_frame(arr, "Insertion Sort (Recursive)", active_indices=[i, i+1])
                return insert_element(i - 1)
        
        arr[i + 1] = last
        draw_frame(arr, "Insertion Sort (Recursive)", active_indices=[i+1])
        return
        
    insert_element(n - 2)


def recursive_merge_sort(arr, start, end):
    if start >= end:
        return

    mid = (start + end) // 2
    recursive_merge_sort(arr, start, mid)
    recursive_merge_sort(arr, mid + 1, end)
    
    def merge(s1, e1, s2, e2, merged_output=None):
        if merged_output is None:
            merged_output = []
            
        if s1 > e1 and s2 > e2:
            return merged_output
            
        current_stats.steps += 1
        
        if s1 > e1:
            merged_output.append(arr[s2])
            draw_frame(arr, "Merge Sort (Recursive)", active_indices=[s2])
            return merge(s1, e1, s2 + 1, e2, merged_output)
        elif s2 > e2:
            merged_output.append(arr[s1])
            draw_frame(arr, "Merge Sort (Recursive)", active_indices=[s1])
            return merge(s1 + 1, e1, s2, e2, merged_output)
        else:
            current_stats.comparisons += 1
            if arr[s1] <= arr[s2]:
                merged_output.append(arr[s1])
                draw_frame(arr, "Merge Sort (Recursive)", active_indices=[s1, s2])
                return merge(s1 + 1, e1, s2, e2, merged_output)
            else:
                merged_output.append(arr[s2])
                draw_frame(arr, "Merge Sort (Recursive)", active_indices=[s1, s2])
                return merge(s1, e1, s2 + 1, e2, merged_output)

    temp_list = merge(start, mid, mid + 1, end)
    
    def write_back(idx, src_idx):
        if src_idx >= len(temp_list):
            return
        current_stats.swaps += 1
        arr[idx] = temp_list[src_idx]
        draw_frame(arr, "Merge Sort (Recursive)", active_indices=[idx])
        write_back(idx + 1, src_idx + 1)
        
    write_back(start, 0)


def recursive_quick_sort(arr, low, high):
    if low >= high:
        return

    def recursive_partition(i, j, pivot_val):
        if j >= high:
            arr[i+1], arr[high] = arr[high], arr[i+1]
            current_stats.swaps += 1
            draw_frame(arr, "Quick Sort (Recursive)", active_indices=[i+1, high])
            return i + 1
            
        current_stats.comparisons += 1
        current_stats.steps += 1
        
        if arr[j] < pivot_val:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            current_stats.swaps += 1
            draw_frame(arr, "Quick Sort (Recursive)", active_indices=[i, j])
        else:
            draw_frame(arr, "Quick Sort (Recursive)", active_indices=[j, high])
            
        return recursive_partition(i, j + 1, pivot_val)

    pivot_idx = recursive_partition(low - 1, low, arr[high])
    
    recursive_quick_sort(arr, low, pivot_idx - 1)
    recursive_quick_sort(arr, pivot_idx + 1, high)


def recursive_heap_sort(arr):
    n = len(arr)
    
    def heapify(size, root):
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2
        
        current_stats.steps += 1
        
        if left < size:
            current_stats.comparisons += 1
            if arr[left] > arr[largest]:
                largest = left
                
        if right < size:
            current_stats.comparisons += 1
            if arr[right] > arr[largest]:
                largest = right
                
        if largest != root:
            arr[root], arr[largest] = arr[largest], arr[root]
            current_stats.swaps += 1
            draw_frame(arr, "Heap Sort (Recursive)", active_indices=[root, largest])
            heapify(size, largest)

    def build_heap(i):
        if i < 0:
            return
        heapify(n, i)
        build_heap(i - 1)

    def extract_elements(i):
        if i <= 0:
            return
        arr[i], arr[0] = arr[0], arr[i]
        current_stats.swaps += 1
        draw_frame(arr, "Heap Sort (Recursive)", active_indices=[0, i])
        heapify(i, 0)
        extract_elements(i - 1)

    build_heap((n // 2) - 1)
    extract_elements(n - 1)


def run_and_profile(algo_func, arr, algo_name, *args):
    global current_stats
    current_stats = Stats()
    
    arr_copy = list(arr)
    current_stats.start_time = time.perf_counter()
    
    algo_func(arr_copy, *args)
    
    current_stats.elapsed_ms = (time.perf_counter() - current_stats.start_time) * 1000
    
    draw_frame(arr_copy, algo_name, sorted_indices=list(range(len(arr_copy))))
    time.sleep(1.0)
    
    return {
        "algo": algo_name,
        "size": len(arr),
        "steps": current_stats.steps,
        "swaps": current_stats.swaps,
        "comps": current_stats.comparisons,
        "time": current_stats.elapsed_ms
    }

def print_summary_table(results):
    clear_screen()
    print(f"\n{BOLD}{CYAN}=========================== FINAL COMPARISON SUMMARY ==========================={RESET}")
    
    headers = ["Algorithm", "Array Size", "Steps", "Swaps", "Comparisons", "Time (ms)"]
    print(f"{BOLD}{headers[0]:<25} | {headers[1]:<10} | {headers[2]:<8} | {headers[3]:<8} | {headers[4]:<12} | {headers[5]:<10}{RESET}")
    print("-" * 85)
    
    min_steps = min(r["steps"] for r in results)
    min_swaps = min(r["swaps"] for r in results)
    min_comps = min(r["comps"] for r in results)
    min_time = min(r["time"] for r in results)
    
    for r in results:
        s_str = f"{GREEN}{r['steps']:<8}{RESET}" if r['steps'] == min_steps else f"{r['steps']:<8}"
        sw_str = f"{GREEN}{r['swaps']:<8}{RESET}" if r['swaps'] == min_swaps else f"{r['swaps']:<8}"
        c_str = f"{GREEN}{r['comps']:<12}{RESET}" if r['comps'] == min_comps else f"{r['comps']:<12}"
        t_str = f"{GREEN}{r['time']:<10.2f}{RESET}" if r['time'] == min_time else f"{r['time']:<10.2f}"
        
        print(f"{r['algo']:<25} | {r['size']:<10} | {s_str} | {sw_str} | {c_str} | {t_str}")
    print("=" * 85)
    print(f"(* {GREEN}Green entries{RESET} highlight the efficiency winners for that column category.)\n")


def main():
    global delay_time
    clear_screen()
    print(f"{BOLD}{CYAN}Welcome to the Recursive Sorting Algorithm Visualizer!{RESET}\n")
    
    try:
        size_input = input("Enter default array size N (e.g., 15): ").strip()
        N = int(size_input) if size_input else 15
    except ValueError:
        print("Invalid sizing. Setting N = 15 automatically.")
        N = 15

    custom_input = input("Provide comma-separated numbers (or press Enter to randomize): ").strip()
    if custom_input:
        try:
            base_array = [int(x.strip()) for x in custom_input.split(",")]
            N = len(base_array)
        except ValueError:
            print("Parsing failed. Generating a randomized array instead.")
            base_array = random.sample(range(5, N * 4 + 5), N)
    else:
        base_array = random.sample(range(5, N * 4 + 5), N)

    speed = input("Choose visual runtime animation speed (slow / normal / fast): ").strip().lower()
    if speed == "slow":
        delay_time = 0.25
    elif speed == "fast":
        delay_time = 0.02
    else:
        delay_time = 0.08  

    results = []
    
    results.append(run_and_profile(recursive_bubble_sort, base_array, "Bubble Sort (Baseline)", len(base_array)))
    results.append(run_and_profile(recursive_insertion_sort, base_array, "Insertion Sort (Baseline)", len(base_array)))
    results.append(run_and_profile(recursive_merge_sort, base_array, "Merge Sort (Recursive)", 0, len(base_array) - 1))
    results.append(run_and_profile(recursive_quick_sort, base_array, "Quick Sort (Recursive)", 0, len(base_array) - 1))
    results.append(run_and_profile(lambda a: recursive_heap_sort(a), base_array, "Heap Sort (Recursive)"))

    print_summary_table(results)

if __name__ == "__main__":
    main()