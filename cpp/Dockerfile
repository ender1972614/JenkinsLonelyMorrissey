# Stage 1: χτίσιμο 
FROM gcc:14 AS builder 
WORKDIR /src 
COPY main.cpp . 
RUN g++ -O2 -static -o hello main.cpp 
# Stage 2: εκτέλεση 
FROM alpine:3.20 
COPY --from=builder /src/hello /usr/local/bin/hello 
CMD ["hello"] 
