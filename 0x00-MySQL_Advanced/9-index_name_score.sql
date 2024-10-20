-- A script to create an INDEX with two keyparts
CREATE INDEX idx_name_first_score ON names (name(1), score);