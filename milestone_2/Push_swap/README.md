Perfect 👍 now you’re thinking **the right way for push_swap**.
I’ll answer exactly what you asked: **what functions you need**, in a **clean logical pipeline**, no extra noise.

---

# 🧠 What you want to do (summarized)

1️⃣ Parse arguments → numbers
2️⃣ Sort numbers with **bubble sort** (only to assign order)
3️⃣ Each number gets an **index / order**
4️⃣ Use stacks A & B
5️⃣ Push from A → B based on order (big on top / small bottom or vice-versa)
6️⃣ Push everything back to A in correct order

This is a **classic indexing strategy** 👍

---

# 🧱 Required data structure

```c
typedef struct s_number
{
	int				num;
	int				order;
	struct s_number		*prev;
	struct s_number		*next;
} 	t_number;
```

Doubly linked list = good choice ✔

---

# 🧩 Functions you WILL need (grouped)

---

## 1️⃣ Parsing & Validation

These run **before any stack operation**.

```c
int		valid_number(char *str);
long	ft_atol(char *str);
void	check_duplicates(t_number *stack);
```

You already have the first two ✔
Duplicates must be checked **after parsing**.

---

## 2️⃣ Stack creation

```c
t_number	*new_node(int num);
void		add_back(t_number **stack, t_number *new);
int			stack_size(t_number *stack);
```

Purpose:

* Build stack A
* Maintain order of input

---

## 3️⃣ Indexing (order assignment)

### 🔹 Step 1: copy numbers to array

```c
int		*stack_to_array(t_number *stack, int size);
```

### 🔹 Step 2: bubble sort the array

```c
void	bubble_sort(int *arr, int size);
```

### 🔹 Step 3: assign index/order

```c
void	assign_order(t_number *stack, int *sorted, int size);
```

📌 After this:

* Smallest number → `order = 0`
* Biggest number → `order = size - 1`

---

## 4️⃣ Stack operations (MANDATORY)

These are **required by subject**:

```c
void	sa(t_number **a);
void	sb(t_number **b);
void	ss(t_number **a, t_number **b);

void	pa(t_number **a, t_number **b);
void	pb(t_number **a, t_number **b);

void	ra(t_number **a);
void	rb(t_number **b);
void	rr(t_number **a, t_number **b);

void	rra(t_number **a);
void	rrb(t_number **b);
void	rrr(t_number **a, t_number **b);
```

Each one must:

* Modify the list
* Print operation name (`write(1, "ra\n", 3)`)

---

## 5️⃣ Moving A → B (based on order)

This is your **main algorithm logic**.

Example functions:

```c
int		find_max_order(t_number *stack);
int		find_min_order(t_number *stack);

void	push_by_order(t_number **a, t_number **b);
```

Example strategy:

* Push smaller half to B
* Rotate A to bring desired order to top
* `pb`
* Repeat

---

## 6️⃣ Returning B → A (sorted)

Since B contains elements ordered by `order`, you do:

```c
void	push_back_to_a(t_number **a, t_number **b);
```

Logic:

* Find biggest `order` in B
* Rotate B until it’s on top
* `pa`
* Repeat

---

## 7️⃣ Utility / helpers (VERY IMPORTANT)

```c
t_number	*find_node_by_order(t_number *stack, int order);
int			is_sorted(t_number *stack);
void		free_stack(t_number **stack);
void		error_exit(void);
```

---

# 🧠 Minimal algorithm flow (this is gold)

```c
parse_args();
build_stack_a();
assign_orders();

if (is_sorted(a))
	exit();

push_a_to_b();
push_b_to_a();
```

---

# 🔥 VERY IMPORTANT (42 tip)

> ❌ Bubble sort is **ONLY for indexing**,
> ❌ NEVER sort the stack itself with bubble sort.

Correctors WILL fail you if you do.

---

## ✅ Final verdict

You’re building:

* ✔ Correct data structure
* ✔ Correct strategy
* ✔ Correct indexing approach

This can easily pass **100 / 500 numbers** if optimized.

---

If you want next:

* I can design **your exact push strategy**
* Or give you **function prototypes only**
* Or help reduce operations count
* Or draw the algorithm visually

Just tell me 🔥
