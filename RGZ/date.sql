CREATE TABLE messages (
  text TEXT NOT NULL,
  pysh_id INT DEFAULT 0,
  on_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP primary key,
  FOREIGN KEY (pysh_id) REFERENCES users(id),
  FOREIGN KEY (on_id) REFERENCES users(id)
);


select * from messages
select * from users

SELECT users.name
FROM messages 
JOIN users ON messages.pysh_id = users.id
WHERE messages.pysh_id = 2 and on_id = 3;

select id from users where name = 'Kate'

INSERT INTO messages (text, pysh_id, on_id) VALUES ('sdfdsfds', 2, 5);

CREATE TABLE users (
  id serial NOT NULL primary key ,
  name CHARACTER VARYING (200) NOT NULL,
  password CHARACTER VARYING (200) NOT NULL
);

INSERT INTO users ( name,password) VALUES  ( 'Vika', 'qwerty'),
  ( 'Alice', 'qwerty'),
 ( 'Bob', 'password123'),
( 'Kate', 'letmein'),
 ( 'Mike', 'secret'),
 ( 'Jane', 'iloveyou'),
 ( 'Tom', 'football'),
 ( 'Mary', 'basketball');


INSERT INTO messages (text, pysh_id, on_id,  created_at) VALUES 
('Привет как дела?', 2, 3, '2022-11-12 21:21:21'),
('Ты кто', 3, 2, '2022-01-01 12:21:21'),
('ААААААА', 2, 3, '2022-01-01 13:40:11'),
('ГДЕ МОИ ПЧЁЛЫ', 3, 4, '2022-01-01 12:14:21'),
('Когда домой', 5, 3, '2022-01-01 12:21:14'),
('ЛЯЛЯЛЯЛ', 7, 8, '2022-01-01 19:21:21'),
('ЯЯЯЯЯЯ', 7, 2, '2022-01-01 12:30:21'),
('Груши вкусные', 5, 6, '2022-12-01 12:40:21'),
('Как так', 6, 3, '2022-01-20 12:20:21'),
('ваяджер', 4, 2, '2022-10-01 10:21:21'),
('gdfgd', 3, 8, '2022-01-14 12:21:23'),
('хахахах=', 3, 4, '2022-06-01 12:35:21'),
('лЯ', 6, 5, '2023-08-01 22:21:21'),
('У меня есть 5', 6, 7, '2022-09-01 23:21:21'),
('Купишь сыр', 5, 3, '2022-01-01 00:21:21'),
('Что', 7, 8, '2022-01-01 14:14:54'),
('Как дела', 4, 5, '2023-01-01 17:21:21'),
('Привет', 5, 6, '2022-01-01 12:53:12'),
('Ку', 4, 3, '2022-01-01 12:11:13'),
('Ау', 5, 3, '2022-01-05 12:21:17'),
('Ясь', 6, 2, '2022-01-01 07:00:21'),
('Щука', 2, 5, '2021-10-01 23:21:21');