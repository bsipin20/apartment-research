package main

import (
	"fmt"
	"net/http"
	"context"

	"github.com/jackc/pgx/v4"
)

func Home(w http.ResponseWriter, r *http.Request){
	fmt.Println("hit home page")
}

func GetLatestPostings(w http.ResponseWriter, r *http.Request) {
	ctx := context.Background()
	conn, _ := pgx.Connect(ctx, "postgresql://admin:quest@localhost:8812/qdb")
	defer conn.Close(ctx)

	// Read top 10 latest posts
	rows, _ := conn.Query(ctx, "SELECT id, price FROM postings4 order by price desc limit 10")
	fmt.Println("Reading from trades table:")
	for rows.Next() {
		var id string
		var price int
		_ = rows.Scan(&id, &price)
		fmt.Println(price, id)
	}

	_ = conn.Close(ctx)
}

