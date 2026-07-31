/*
order_reviews
-> review_id TEXT NOT NULL
-> order_id TEXT NOT NULL
-> review_score INTEGER NOT NULL CHECK >=1 and less then <= 5
-> review_comment_title TEXT 
-> review_comment_message TEXT
-> review_creation_date TIMESTAMP NOT NULL
-> review_answer_timestamp TIMESTAMP NOT NULL
-> review_id and order_id creates a primary key
*/ 

CREATE TABLE staging.order_reviews (
    review_id TEXT NOT NULL,
    order_id TEXT NOT NULL,
    review_score INTEGER NOT NULL,
    review_comment_title TEXT,
    review_comment_message TEXT,
    review_creation_date TIMESTAMP NOT NULL,
    review_answer_timestamp TIMESTAMP NOT NULL,
    CONSTRAINT pk_order_reviews 
    PRIMARY KEY (
        review_id, order_id
    ),
    CONSTRAINT chk_review_score
        CHECK  (
            review_score >=1 and review_score<=5
        )  
)