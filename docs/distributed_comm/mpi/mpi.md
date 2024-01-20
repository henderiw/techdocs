# MPI introduction

```c
// setup ->
MPI_init(int *argc, char ****argv)
// tear down
MPI_Finalze()
// total processes
MPI_Comm_Size(MPI_Comm comm, int *size)
// we we are -> global index for each of the processes that participate
// local process index -> pointer to allow the function to change the rank info
MPI_Comm_rank(MPI_Comm comm, int *rank)
```

```c
int
main (int argc, char **argv)
{
    int num_procs;
    int rank;

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &num_procs)
    MPI_Comm_size(MPI_COMM_WORLD, &num_procs)
    printf("%d: hello (p=%d)\n", rank, num)

    /* stuff */

    MPI_Finalze()
}

```

both sides of the communication need to be coordinated

```c
// Send
// buf: beginning of the data
// count: 10
// datatype: MPI_CHAR, MPI_SIGNED_CHAR, MPI_INT, MPI_LONG, MPI_FLOAT, MPI_LONG_LONG
// dest -> rank (process)
// tag -> (hint message of type x)
// comm -> communicator
int MPI_Send(void *buf, int count, MPI_Datatype datatype, int dest, int tag, MPI_Comm comm)

// Receive
// buf: memory where to store
// count: #elements
// datatype
// source: rnank of the process i want to receive from
// tag -> (hint of message of type x)
// comm
// MPI_Status (MPI_Source (rank))
int MPI_Recv(void *buf, int count, MPI_Datatype datatype, int dest, int tag, MPI_Comm comm, MPI_Status *status)
```

round robin program

```c
int
main (int argc, char **argv)
{
    int num_procs;
    int rank;

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &num_procs)
    MPI_Comm_size(MPI_COMM_WORLD, &num_procs)
   
    printf("%d: hello (p=%d)\n", rank, num)
    round_robin(rank, num_procs);
    printf("%d: goodbye\n", rank)

    MPI_Finalze()
}

void 
round_robin(int rank, int procs)
{
    long int rand_mine, rand_prev; // store the data
    int rank_next = (rank + 1) % procs; // get the next rank
    int prev_rank = rank == 0 ? procs =1 : ramk -1;
    MPI_Status status;

    srandom(time(NULL) + rank);
    rand_mine = random() / (RAND_MAX / 100);
    printf("%d: random is %ld\n", rank, rand_mine);

    // divide processes in 2 groups
    if (rank % 2 == 0 ) {
        // address of rand_mine, 1 entry, datatype LONG
        MPI_Send((void *)&rand_mine, 1, MPI_LONG, rank_next, 1, MPI_COMM_WORLD);

        MPI_Recv((void *)&rand_prev, 1, MPI_LONG, rank_prev, 1, MPI_COMM_WORLD, &status);
    } else {
        MPI_Recv((void *)&rand_prev, 1, MPI_LONG, rank_prev, 1, MPI_COMM_WORLD, &status);

        MPI_Send((void *)&rand_mine, 1, MPI_LONG, rank_next, 1, MPI_COMM_WORLD);
    }
}
```