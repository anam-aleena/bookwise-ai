"""
Comprehensive book database with summaries and reading links
"""

BOOKS_DATABASE = {
    1: {
        "title": "Brave New World",
        "author": "Aldous Huxley",
        "genre": "Science Fiction",
        "year": 1932,
        "pages": 311,
        "summary": "A haunting vision of a future society where humans are genetically engineered and conditioned to be content with their lot. Explores themes of technology, control, and the cost of happiness in a world without pain or struggle.",
        "read_link": "https://www.gutenberg.org/ebooks/author/3046",
        "cover_color": "#1a1a2e"
    },
    2: {
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "year": 1954,
        "pages": 1178,
        "summary": "An epic tale of good versus evil in the magical realm of Middle-earth. Follow Frodo Baggins and his fellowship on their perilous quest to destroy the One Ring and save their world from the Dark Lord Sauron.",
        "read_link": "https://www.amazon.com/Lord-Rings-J-R-R-Tolkien/dp/0544003411",
        "cover_color": "#2d3436"
    },
    3: {
        "title": "Paper Towns",
        "author": "John Green",
        "genre": "Young Adult",
        "year": 2008,
        "pages": 305,
        "summary": "A captivating mystery about Quentin's journey to find his enigmatic neighbor Margo Roth Spiegelman after she disappears. A thoughtful exploration of identity, perception, and the danger of idealizing people.",
        "read_link": "https://www.amazon.com/Paper-Towns-John-Green/dp/014241493X",
        "cover_color": "#00b894"
    },
    4: {
        "title": "Crime and Punishment",
        "author": "Fyodor Dostoevsky",
        "genre": "Psychological Fiction",
        "year": 1866,
        "pages": 671,
        "summary": "A profound psychological exploration of guilt, morality, and redemption. Follow Raskolnikov, a destitute student who commits a murder and struggles with his conscience in 19th century St. Petersburg.",
        "read_link": "https://www.gutenberg.org/ebooks/2554",
        "cover_color": "#6c5ce7"
    },
    5: {
        "title": "The Maze Runner",
        "author": "James Dashner",
        "genre": "Dystopian",
        "year": 2009,
        "pages": 374,
        "summary": "Thomas wakes up in a mysterious maze with no memory of his past. With a group of boys called the Gladers, he must uncover the secrets of the maze before it's too late. A thrilling adventure of survival and mystery.",
        "read_link": "https://www.amazon.com/Maze-Runner-Book-1/dp/0385737955",
        "cover_color": "#636e72"
    },
    6: {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Fiction",
        "year": 1925,
        "pages": 180,
        "summary": "A tragic tale of Jay Gatsby's obsessive pursuit of Daisy Buchanan in 1920s America. A masterful exploration of wealth, class, love, and the American Dream's corruption during the Jazz Age.",
        "read_link": "https://www.gutenberg.org/ebooks/64317",
        "cover_color": "#fdcb6e"
    },
    7: {
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "genre": "Fantasy",
        "year": 1997,
        "pages": 309,
        "summary": "Orphan Harry Potter discovers he's a wizard and enters the magical world of Hogwarts School. Begin the beloved journey of friendship, magic, and the fight against dark forces that captivated millions worldwide.",
        "read_link": "https://www.amazon.com/Harry-Potter-Sorcerers-Stone-Rowling/dp/059035342X",
        "cover_color": "#e17055"
    },
    8: {
        "title": "The Handmaid's Tale",
        "author": "Margaret Atwood",
        "genre": "Dystopian",
        "year": 1985,
        "pages": 311,
        "summary": "In the totalitarian Republic of Gilead, Offred serves as a handmaid forced to bear children. A chilling portrayal of women's oppression and a powerful warning about religious extremism and authoritarian control.",
        "read_link": "https://www.amazon.com/Handmaids-Tale-Margaret-Atwood/dp/038549081X",
        "cover_color": "#d63031"
    },
    9: {
        "title": "War and Peace",
        "author": "Leo Tolstoy",
        "genre": "Historical Fiction",
        "year": 1869,
        "pages": 1225,
        "summary": "An epic chronicle of Russian society during the Napoleonic Wars. Through the intertwined lives of five aristocratic families, Tolstoy weaves a masterpiece exploring war, love, family, and the meaning of life.",
        "read_link": "https://www.gutenberg.org/ebooks/2600",
        "cover_color": "#0984e3"
    },
    10: {
        "title": "Gone Girl",
        "author": "Gillian Flynn",
        "genre": "Thriller",
        "year": 2012,
        "pages": 415,
        "summary": "When Amy Dunne disappears on her fifth wedding anniversary, suspicion falls on her husband Nick. A twisted psychological thriller with unreliable narrators that will keep you guessing until the shocking end.",
        "read_link": "https://www.amazon.com/Gone-Girl-Gillian-Flynn/dp/0307588378",
        "cover_color": "#2d3436"
    },
    11: {
        "title": "Fahrenheit 451",
        "author": "Ray Bradbury",
        "genre": "Science Fiction",
        "year": 1953,
        "pages": 158,
        "summary": "In a future where books are banned and burned, fireman Guy Montag begins to question everything. A powerful warning about censorship, conformity, and the importance of critical thinking in society.",
        "read_link": "https://www.amazon.com/Fahrenheit-451-Ray-Bradbury/dp/1451673310",
        "cover_color": "#e74c3c"
    },
    12: {
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "year": 1949,
        "pages": 328,
        "summary": "Winston Smith lives in a totalitarian state where Big Brother watches everything. A haunting exploration of surveillance, propaganda, and thought control that remains disturbingly relevant today.",
        "read_link": "https://www.amazon.com/1984-Signet-Classics-George-Orwell/dp/0451524934",
        "cover_color": "#2c3e50"
    },
    13: {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "genre": "Fiction",
        "year": 1988,
        "pages": 197,
        "summary": "Young shepherd Santiago embarks on a journey to find treasure at the Egyptian pyramids. A timeless fable about following your dreams, listening to your heart, and discovering your Personal Legend.",
        "read_link": "https://www.amazon.com/Alchemist-Paulo-Coelho/dp/0062315005",
        "cover_color": "#f39c12"
    },
    14: {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "year": 1813,
        "pages": 279,
        "summary": "The spirited Elizabeth Bennet clashes with the proud Mr. Darcy in Regency-era England. A witty and timeless exploration of love, class, and the dangers of making hasty judgments about others.",
        "read_link": "https://www.gutenberg.org/ebooks/1342",
        "cover_color": "#e84393"
    },
    15: {
        "title": "An Abundance of Katherines",
        "author": "John Green",
        "genre": "Young Adult",
        "year": 2006,
        "pages": 227,
        "summary": "Child prodigy Colin has been dumped by nineteen Katherines. On a road trip with his best friend, he sets out to prove a theorem that will predict the future of any relationship. A witty tale of love and self-discovery.",
        "read_link": "https://www.amazon.com/Abundance-Katherines-John-Green/dp/014241070X",
        "cover_color": "#74b9ff"
    },
    16: {
        "title": "Neuromancer",
        "author": "William Gibson",
        "genre": "Science Fiction",
        "year": 1984,
        "pages": 271,
        "summary": "Case, a washed-up computer hacker, is hired for one last job in the matrix. The groundbreaking cyberpunk novel that predicted the internet age and coined the term 'cyberspace.' Essential reading for tech enthusiasts.",
        "read_link": "https://www.amazon.com/Neuromancer-William-Gibson/dp/0441569595",
        "cover_color": "#00cec9"
    },
    17: {
        "title": "The Brothers Karamazov",
        "author": "Fyodor Dostoevsky",
        "genre": "Philosophical Fiction",
        "year": 1880,
        "pages": 796,
        "summary": "The story of three brothers and their father's murder explores faith, doubt, morality, and free will. Dostoevsky's final masterpiece and one of the greatest novels ever written about the human condition.",
        "read_link": "https://www.gutenberg.org/ebooks/28054",
        "cover_color": "#a29bfe"
    },
    18: {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Fiction",
        "year": 1951,
        "pages": 214,
        "summary": "Teenager Holden Caulfield recounts his experiences in New York City after being expelled from prep school. A profound exploration of teenage alienation, identity, and the painful transition to adulthood.",
        "read_link": "https://www.amazon.com/Catcher-Rye-J-D-Salinger/dp/0316769177",
        "cover_color": "#ff7675"
    },
    19: {
        "title": "Looking for Alaska",
        "author": "John Green",
        "genre": "Young Adult",
        "year": 2005,
        "pages": 221,
        "summary": "Miles 'Pudge' Halter leaves his ordinary life for boarding school seeking the Great Perhaps. There he meets the captivating Alaska Young and learns about love, loss, and the mystery of human connection.",
        "read_link": "https://www.amazon.com/Looking-Alaska-John-Green/dp/0142402516",
        "cover_color": "#55efc4"
    },
    20: {
        "title": "Dune",
        "author": "Frank Herbert",
        "genre": "Science Fiction",
        "year": 1965,
        "pages": 688,
        "summary": "Young Paul Atreides becomes embroiled in a struggle for control of the desert planet Arrakis. An epic saga of politics, religion, and ecology that redefined the science fiction genre for generations.",
        "read_link": "https://www.amazon.com/Dune-Frank-Herbert/dp/0441172717",
        "cover_color": "#f9ca24"
    },
    21: {
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
        "genre": "Dystopian",
        "year": 2008,
        "pages": 374,
        "summary": "In a dark future, Katniss Everdeen volunteers to fight in the deadly Hunger Games to save her sister. A gripping tale of survival, rebellion, and media manipulation in a totalitarian society.",
        "read_link": "https://www.amazon.com/Hunger-Games-Book-1/dp/0439023521",
        "cover_color": "#e55039"
    },
    22: {
        "title": "Lord of the Flies",
        "author": "William Golding",
        "genre": "Fiction",
        "year": 1954,
        "pages": 224,
        "summary": "Boys stranded on a deserted island descend into savagery as civilization crumbles. A disturbing allegory about human nature, the thin veneer of civilization, and the darkness that lurks within us all.",
        "read_link": "https://www.amazon.com/Lord-Flies-William-Golding/dp/0399501487",
        "cover_color": "#636e72"
    },
    23: {
        "title": "Ender's Game",
        "author": "Orson Scott Card",
        "genre": "Science Fiction",
        "year": 1985,
        "pages": 324,
        "summary": "Child genius Ender Wiggin is recruited to Battle School to save humanity from an alien invasion. A thought-provoking tale of strategy, morality, and the weight of command that challenges our ethics.",
        "read_link": "https://www.amazon.com/Enders-Game-Ender-Quintet-1/dp/0812550706",
        "cover_color": "#2d3436"
    },
    24: {
        "title": "The Odyssey",
        "author": "Homer",
        "genre": "Epic Poetry",
        "year": -700,
        "pages": 384,
        "summary": "Odysseus journeys home after the Trojan War, facing monsters, gods, and temptations. The foundational adventure story of Western literature, exploring heroism, loyalty, and the longing for home.",
        "read_link": "https://www.gutenberg.org/ebooks/1727",
        "cover_color": "#0984e3"
    },
    25: {
        "title": "Divergent",
        "author": "Veronica Roth",
        "genre": "Dystopian",
        "year": 2011,
        "pages": 487,
        "summary": "In a divided Chicago, Tris must choose between family and identity when she discovers she's Divergent—a threat to the system. An action-packed exploration of choice, belonging, and defying expectations.",
        "read_link": "https://www.amazon.com/Divergent-Veronica-Roth/dp/0062387243",
        "cover_color": "#3867d6"
    },
    26: {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Fiction",
        "year": 1960,
        "pages": 281,
        "summary": "Scout Finch witnesses her father defend a Black man accused of a terrible crime in 1930s Alabama. A profound exploration of racial injustice, moral courage, and the loss of innocence in the American South.",
        "read_link": "https://www.amazon.com/Kill-Mockingbird-Harper-Lee/dp/0060935464",
        "cover_color": "#2d3436"
    },
    27: {
        "title": "The Fault in Our Stars",
        "author": "John Green",
        "genre": "Romance",
        "year": 2012,
        "pages": 313,
        "summary": "Hazel and Augustus, two teenagers with cancer, fall in love and embark on a journey to Amsterdam. A beautiful, heart-wrenching story about love, loss, and what it means to be truly alive.",
        "read_link": "https://www.amazon.com/Fault-Our-Stars-John-Green/dp/014242417X",
        "cover_color": "#74b9ff"
    },
    28: {
        "title": "Great Expectations",
        "author": "Charles Dickens",
        "genre": "Fiction",
        "year": 1861,
        "pages": 544,
        "summary": "Orphan Pip rises from humble origins to become a gentleman, only to discover the true source of his fortune. A timeless tale of ambition, love, and redemption in Victorian England.",
        "read_link": "https://www.gutenberg.org/ebooks/1400",
        "cover_color": "#8e44ad"
    },
    29: {
        "title": "The Iliad",
        "author": "Homer",
        "genre": "Epic Poetry",
        "year": -750,
        "pages": 683,
        "summary": "The rage of Achilles and the siege of Troy come alive in this epic tale of war, honor, and fate. The foundational work of Western literature that shaped our understanding of heroism and tragedy.",
        "read_link": "https://www.gutenberg.org/ebooks/2199",
        "cover_color": "#c0392b"
    },
    30: {
        "title": "The Adventures of Huckleberry Finn",
        "author": "Mark Twain",
        "genre": "Fiction",
        "year": 1884,
        "pages": 366,
        "summary": "Huck Finn escapes civilization and floats down the Mississippi with escaped slave Jim. A rollicking adventure and sharp satire that confronts America's troubled relationship with race and freedom.",
        "read_link": "https://www.gutenberg.org/ebooks/76",
        "cover_color": "#27ae60"
    },
    31: {
        "title": "Animal Farm",
        "author": "George Orwell",
        "genre": "Political Fiction",
        "year": 1945,
        "pages": 112,
        "summary": "Farm animals overthrow their human master, but the pigs' revolution goes terribly wrong. A brilliant allegory about power, corruption, and how revolutionary ideals become perverted by authoritarian leaders.",
        "read_link": "https://www.amazon.com/Animal-Farm-George-Orwell/dp/0451526341",
        "cover_color": "#e74c3c"
    },
    32: {
        "title": "The Hitchhiker's Guide to the Galaxy",
        "author": "Douglas Adams",
        "genre": "Science Fiction",
        "year": 1979,
        "pages": 193,
        "summary": "Arthur Dent escapes Earth's destruction and hitchhikes through the galaxy with his alien friend Ford. A hilarious cosmic journey filled with absurd humor and philosophical musings about life, the universe, and everything.",
        "read_link": "https://www.amazon.com/Hitchhikers-Guide-Galaxy-Douglas-Adams/dp/0345391802",
        "cover_color": "#00b894"
    },
    33: {
        "title": "Anna Karenina",
        "author": "Leo Tolstoy",
        "genre": "Fiction",
        "year": 1877,
        "pages": 864,
        "summary": "Anna's passionate affair with Count Vronsky leads to tragedy in 19th century Russian society. Tolstoy's exploration of love, jealousy, and social convention remains one of literature's greatest achievements.",
        "read_link": "https://www.gutenberg.org/ebooks/1399",
        "cover_color": "#d63031"
    },
    34: {
        "title": "The Martian",
        "author": "Andy Weir",
        "genre": "Science Fiction",
        "year": 2011,
        "pages": 369,
        "summary": "Astronaut Mark Watney is stranded alone on Mars and must science his way to survival. A gripping, scientifically accurate tale of human ingenuity, humor, and the will to live against impossible odds.",
        "read_link": "https://www.amazon.com/Martian-Andy-Weir/dp/0553418025",
        "cover_color": "#e17055"
    },
    35: {
        "title": "Moby Dick",
        "author": "Herman Melville",
        "genre": "Fiction",
        "year": 1851,
        "pages": 720,
        "summary": "Captain Ahab's obsessive hunt for the white whale leads his crew to destruction. An epic exploration of obsession, fate, and humanity's struggle against nature that transcends its maritime setting.",
        "read_link": "https://www.gutenberg.org/ebooks/2701",
        "cover_color": "#0984e3"
    },
    36: {
        "title": "Will Grayson, Will Grayson",
        "author": "John Green & David Levithan",
        "genre": "Young Adult",
        "year": 2010,
        "pages": 310,
        "summary": "Two teens named Will Grayson meet by chance in Chicago, and their lives become intertwined. A collaborative novel about identity, friendship, and the courage to be yourself in a world of expectations.",
        "read_link": "https://www.amazon.com/Will-Grayson-John-Green/dp/014241847X",
        "cover_color": "#a29bfe"
    },
    37: {
        "title": "Foundation",
        "author": "Isaac Asimov",
        "genre": "Science Fiction",
        "year": 1951,
        "pages": 244,
        "summary": "Mathematician Hari Seldon predicts the fall of the Galactic Empire and establishes the Foundation to preserve knowledge. A landmark of science fiction exploring the mathematics of history and civilization.",
        "read_link": "https://www.amazon.com/Foundation-Isaac-Asimov/dp/0553293354",
        "cover_color": "#6c5ce7"
    },
    38: {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "year": 1937,
        "pages": 310,
        "summary": "Bilbo Baggins is swept into an adventure with thirteen dwarves to reclaim their treasure from a dragon. The beloved prelude to Lord of the Rings that introduced readers to the enchanting world of Middle-earth.",
        "read_link": "https://www.amazon.com/Hobbit-J-R-R-Tolkien/dp/054792822X",
        "cover_color": "#00b894"
    },
    39: {
        "title": "Wuthering Heights",
        "author": "Emily Brontë",
        "genre": "Gothic Fiction",
        "year": 1847,
        "pages": 416,
        "summary": "The passionate and destructive love between Heathcliff and Catherine haunts the moors of Yorkshire. A dark, powerful novel about obsession, revenge, and love that transcends death and social boundaries.",
        "read_link": "https://www.gutenberg.org/ebooks/768",
        "cover_color": "#2d3436"
    },
    40: {
        "title": "Jane Eyre",
        "author": "Charlotte Brontë",
        "genre": "Gothic Fiction",
        "year": 1847,
        "pages": 532,
        "summary": "Orphan Jane becomes governess at mysterious Thornfield Hall and falls for the enigmatic Mr. Rochester. A groundbreaking story of a woman's independence, love, and moral integrity in Victorian England.",
        "read_link": "https://www.gutenberg.org/ebooks/1260",
        "cover_color": "#9b59b6"
    },
    41: {
        "title": "The Scarlet Letter",
        "author": "Nathaniel Hawthorne",
        "genre": "Historical Fiction",
        "year": 1850,
        "pages": 272,
        "summary": "Hester Prynne wears a scarlet 'A' for adultery in Puritan Massachusetts while hiding her lover's identity. A powerful exploration of sin, guilt, and redemption in colonial America's harsh moral landscape.",
        "read_link": "https://www.gutenberg.org/ebooks/25344",
        "cover_color": "#c0392b"
    },
    42: {
        "title": "The Picture of Dorian Gray",
        "author": "Oscar Wilde",
        "genre": "Gothic Fiction",
        "year": 1890,
        "pages": 254,
        "summary": "A beautiful young man's portrait ages while he remains eternally youthful—at a terrible cost. Wilde's only novel is a dazzling exploration of beauty, corruption, and the price of eternal youth.",
        "read_link": "https://www.gutenberg.org/ebooks/174",
        "cover_color": "#8e44ad"
    },
    43: {
        "title": "Frankenstein",
        "author": "Mary Shelley",
        "genre": "Gothic Fiction",
        "year": 1818,
        "pages": 280,
        "summary": "Scientist Victor Frankenstein creates life, only to be haunted by his monstrous creation. The original science fiction novel that questions the ethics of creation and the nature of humanity itself.",
        "read_link": "https://www.gutenberg.org/ebooks/84",
        "cover_color": "#2d3436"
    },
    44: {
        "title": "Dracula",
        "author": "Bram Stoker",
        "genre": "Horror",
        "year": 1897,
        "pages": 418,
        "summary": "Jonathan Harker's encounter with Count Dracula unleashes ancient evil upon Victorian England. The definitive vampire novel that shaped our modern conception of the undead and gothic horror.",
        "read_link": "https://www.gutenberg.org/ebooks/345",
        "cover_color": "#c0392b"
    },
    45: {
        "title": "The Shining",
        "author": "Stephen King",
        "genre": "Horror",
        "year": 1977,
        "pages": 447,
        "summary": "The Torrance family winters at the haunted Overlook Hotel, where dark forces prey on young Danny's psychic abilities. King's masterpiece of psychological horror that explores isolation, addiction, and supernatural evil.",
        "read_link": "https://www.amazon.com/Shining-Stephen-King/dp/0307743659",
        "cover_color": "#e74c3c"
    },
    46: {
        "title": "It",
        "author": "Stephen King",
        "genre": "Horror",
        "year": 1986,
        "pages": 1138,
        "summary": "Seven friends confront an ancient evil that takes the form of a terrifying clown in their hometown. An epic tale of childhood fears, friendship, and the power of memory against unspeakable horror.",
        "read_link": "https://www.amazon.com/It-Novel-Stephen-King/dp/1501142976",
        "cover_color": "#d63031"
    },
    47: {
        "title": "The Stand",
        "author": "Stephen King",
        "genre": "Horror",
        "year": 1978,
        "pages": 1153,
        "summary": "After a pandemic wipes out civilization, survivors gather for a final battle between good and evil. King's epic apocalyptic novel explores the best and worst of humanity in the face of destruction.",
        "read_link": "https://www.amazon.com/Stand-Stephen-King/dp/0307743683",
        "cover_color": "#2d3436"
    },
    48: {
        "title": "Ready Player One",
        "author": "Ernest Cline",
        "genre": "Science Fiction",
        "year": 2011,
        "pages": 374,
        "summary": "Wade Watts searches for an Easter egg hidden in a virtual reality world that will grant him ultimate power. A nostalgic adventure packed with 1980s pop culture references and high-stakes gaming.",
        "read_link": "https://www.amazon.com/Ready-Player-One-Ernest-Cline/dp/0307887448",
        "cover_color": "#6c5ce7"
    },
    49: {
        "title": "The Girl with the Dragon Tattoo",
        "author": "Stieg Larsson",
        "genre": "Thriller",
        "year": 2005,
        "pages": 465,
        "summary": "Journalist Mikael Blomkvist and hacker Lisbeth Salander investigate a decades-old disappearance. A gripping thriller exposing dark secrets of wealth and power in Swedish society.",
        "read_link": "https://www.amazon.com/Girl-Dragon-Tattoo-Millennium/dp/0307454541",
        "cover_color": "#2d3436"
    },
    50: {
        "title": "The Da Vinci Code",
        "author": "Dan Brown",
        "genre": "Thriller",
        "year": 2003,
        "pages": 454,
        "summary": "Robert Langdon races to solve a murder in the Louvre that leads to secrets hidden by Leonardo da Vinci. A controversial thriller blending art history, religious conspiracy, and non-stop action.",
        "read_link": "https://www.amazon.com/Vinci-Code-Dan-Brown/dp/0307474275",
        "cover_color": "#9b59b6"
    },
    51: {
        "title": "The Kite Runner",
        "author": "Khaled Hosseini",
        "genre": "Fiction",
        "year": 2003,
        "pages": 371,
        "summary": "Amir returns to Taliban-controlled Afghanistan to rescue his childhood friend's son. A powerful story of guilt, redemption, and the bonds of friendship against the backdrop of a troubled nation.",
        "read_link": "https://www.amazon.com/Kite-Runner-Khaled-Hosseini/dp/159463193X",
        "cover_color": "#e17055"
    },
    52: {
        "title": "A Thousand Splendid Suns",
        "author": "Khaled Hosseini",
        "genre": "Fiction",
        "year": 2007,
        "pages": 372,
        "summary": "Two Afghan women from different generations find strength in their bond amid decades of war. An epic tale of love, sacrifice, and hope that illuminates the resilience of women in Afghanistan.",
        "read_link": "https://www.amazon.com/Thousand-Splendid-Suns-Khaled-Hosseini/dp/159448385X",
        "cover_color": "#fdcb6e"
    },
    53: {
        "title": "Life of Pi",
        "author": "Yann Martel",
        "genre": "Fiction",
        "year": 2001,
        "pages": 319,
        "summary": "After a shipwreck, Pi Patel survives 227 days on a lifeboat with a Bengal tiger. An imaginative tale of survival, faith, and storytelling that questions the nature of truth and belief.",
        "read_link": "https://www.amazon.com/Life-Pi-Yann-Martel/dp/0156027321",
        "cover_color": "#0984e3"
    },
    54: {
        "title": "The Book Thief",
        "author": "Markus Zusak",
        "genre": "Historical Fiction",
        "year": 2005,
        "pages": 552,
        "summary": "Narrated by Death, this is the story of Liesel, a girl who steals books in Nazi Germany. A haunting and beautiful meditation on the power of words and stories in the darkest of times.",
        "read_link": "https://www.amazon.com/Book-Thief-Markus-Zusak/dp/0375842209",
        "cover_color": "#636e72"
    },
    55: {
        "title": "The Help",
        "author": "Kathryn Stockett",
        "genre": "Fiction",
        "year": 2009,
        "pages": 451,
        "summary": "Black maids and a young white woman collaborate on a book exposing the truth of their lives in 1960s Mississippi. A moving story of courage, friendship, and finding your voice in the segregated South.",
        "read_link": "https://www.amazon.com/Help-Kathryn-Stockett/dp/0425232204",
        "cover_color": "#e84393"
    },
    56: {
        "title": "The Secret Garden",
        "author": "Frances Hodgson Burnett",
        "genre": "Fiction",
        "year": 1911,
        "pages": 331,
        "summary": "Orphan Mary discovers a hidden garden at her uncle's mansion and works to restore it to beauty. A timeless story of healing, friendship, and the transformative power of nature and love.",
        "read_link": "https://www.gutenberg.org/ebooks/113",
        "cover_color": "#00b894"
    },
    57: {
        "title": "Little Women",
        "author": "Louisa May Alcott",
        "genre": "Fiction",
        "year": 1868,
        "pages": 449,
        "summary": "The four March sisters—Meg, Jo, Beth, and Amy—navigate growing up during the Civil War era. A beloved classic celebrating sisterhood, individuality, and the dreams of young women.",
        "read_link": "https://www.gutenberg.org/ebooks/514",
        "cover_color": "#e84393"
    },
    58: {
        "title": "A Tale of Two Cities",
        "author": "Charles Dickens",
        "genre": "Historical Fiction",
        "year": 1859,
        "pages": 489,
        "summary": "Love and sacrifice intertwine against the backdrop of the French Revolution in London and Paris. Dickens' tale of resurrection and redemption opens with literature's most famous first line.",
        "read_link": "https://www.gutenberg.org/ebooks/98",
        "cover_color": "#d63031"
    },
    59: {
        "title": "Oliver Twist",
        "author": "Charles Dickens",
        "genre": "Fiction",
        "year": 1838,
        "pages": 608,
        "summary": "Orphan Oliver escapes the workhouse only to fall in with a gang of pickpockets in Victorian London. Dickens' social critique exposes the cruel treatment of the poor while telling an unforgettable story.",
        "read_link": "https://www.gutenberg.org/ebooks/730",
        "cover_color": "#2d3436"
    },
    60: {
        "title": "David Copperfield",
        "author": "Charles Dickens",
        "genre": "Fiction",
        "year": 1850,
        "pages": 882,
        "summary": "The autobiographical tale of David's journey from abused orphan to successful writer. Dickens' favorite among his novels, filled with memorable characters and Victorian social commentary.",
        "read_link": "https://www.gutenberg.org/ebooks/766",
        "cover_color": "#8e44ad"
    },
    61: {
        "title": "The Adventures of Sherlock Holmes",
        "author": "Arthur Conan Doyle",
        "genre": "Mystery",
        "year": 1892,
        "pages": 307,
        "summary": "The world's greatest detective solves seemingly impossible cases from 221B Baker Street. Twelve brilliant short stories featuring the legendary Holmes and his faithful companion Dr. Watson.",
        "read_link": "https://www.gutenberg.org/ebooks/1661",
        "cover_color": "#2d3436"
    },
    62: {
        "title": "The Hound of the Baskervilles",
        "author": "Arthur Conan Doyle",
        "genre": "Mystery",
        "year": 1902,
        "pages": 256,
        "summary": "Sherlock Holmes investigates a supernatural hound haunting the Baskerville family on the misty moors. The most famous Holmes novel combines gothic atmosphere with brilliant deductive reasoning.",
        "read_link": "https://www.gutenberg.org/ebooks/2852",
        "cover_color": "#636e72"
    },
    63: {
        "title": "Murder on the Orient Express",
        "author": "Agatha Christie",
        "genre": "Mystery",
        "year": 1934,
        "pages": 256,
        "summary": "Detective Hercule Poirot investigates a murder on a snowbound train with twelve suspects. Christie's most famous mystery features one of literature's most surprising and ingenious solutions.",
        "read_link": "https://www.amazon.com/Murder-Orient-Express-Hercule-Mysteries/dp/0062693662",
        "cover_color": "#6c5ce7"
    },
    64: {
        "title": "And Then There Were None",
        "author": "Agatha Christie",
        "genre": "Mystery",
        "year": 1939,
        "pages": 272,
        "summary": "Ten strangers are lured to an island where they begin dying one by one according to a nursery rhyme. Christie's bestselling novel is a masterpiece of suspense and misdirection.",
        "read_link": "https://www.amazon.com/Then-There-Were-None/dp/0062073486",
        "cover_color": "#2d3436"
    },
    65: {
        "title": "Rebecca",
        "author": "Daphne du Maurier",
        "genre": "Gothic Fiction",
        "year": 1938,
        "pages": 380,
        "summary": "A young bride arrives at Manderley only to be haunted by her husband's glamorous first wife. A masterful gothic romance exploring jealousy, identity, and the power of memory.",
        "read_link": "https://www.amazon.com/Rebecca-Daphne-du-Maurier/dp/0380730405",
        "cover_color": "#9b59b6"
    },
    66: {
        "title": "The Count of Monte Cristo",
        "author": "Alexandre Dumas",
        "genre": "Adventure",
        "year": 1844,
        "pages": 1276,
        "summary": "Wrongly imprisoned Edmond Dantès escapes and enacts elaborate revenge on those who betrayed him. The ultimate tale of revenge and redemption, filled with adventure, romance, and intrigue.",
        "read_link": "https://www.gutenberg.org/ebooks/1184",
        "cover_color": "#f39c12"
    },
    67: {
        "title": "The Three Musketeers",
        "author": "Alexandre Dumas",
        "genre": "Adventure",
        "year": 1844,
        "pages": 625,
        "summary": "Young D'Artagnan joins the legendary musketeers in swashbuckling adventures in 17th century France. All for one and one for all—the quintessential adventure novel of friendship and honor.",
        "read_link": "https://www.gutenberg.org/ebooks/1257",
        "cover_color": "#0984e3"
    },
    68: {
        "title": "Treasure Island",
        "author": "Robert Louis Stevenson",
        "genre": "Adventure",
        "year": 1883,
        "pages": 292,
        "summary": "Young Jim Hawkins discovers a treasure map and embarks on a perilous voyage with pirates. The classic adventure story that defined the pirate genre with unforgettable characters like Long John Silver.",
        "read_link": "https://www.gutenberg.org/ebooks/120",
        "cover_color": "#00b894"
    },
    69: {
        "title": "The Call of the Wild",
        "author": "Jack London",
        "genre": "Adventure",
        "year": 1903,
        "pages": 128,
        "summary": "A domesticated dog is stolen and thrust into the brutal Yukon gold rush as a sled dog. A powerful tale of survival and the primal instincts that lie dormant within all creatures.",
        "read_link": "https://www.gutenberg.org/ebooks/215",
        "cover_color": "#2d3436"
    },
    70: {
        "title": "White Fang",
        "author": "Jack London",
        "genre": "Adventure",
        "year": 1906,
        "pages": 298,
        "summary": "A wild wolf-dog's journey from the wilderness to civilization in the frozen Yukon. London's companion piece to The Call of the Wild explores the transformative power of love and kindness.",
        "read_link": "https://www.gutenberg.org/ebooks/910",
        "cover_color": "#dfe6e9"
    },
    71: {
        "title": "The Jungle Book",
        "author": "Rudyard Kipling",
        "genre": "Adventure",
        "year": 1894,
        "pages": 277,
        "summary": "Mowgli, a boy raised by wolves in the Indian jungle, learns the law of the jungle from animal friends. Timeless tales of adventure, friendship, and belonging that enchant readers of all ages.",
        "read_link": "https://www.gutenberg.org/ebooks/236",
        "cover_color": "#27ae60"
    },
    72: {
        "title": "Around the World in Eighty Days",
        "author": "Jules Verne",
        "genre": "Adventure",
        "year": 1872,
        "pages": 312,
        "summary": "Phileas Fogg wagers he can circumnavigate the globe in just eighty days. Verne's thrilling race against time combines adventure, humor, and a celebration of human ingenuity.",
        "read_link": "https://www.gutenberg.org/ebooks/103",
        "cover_color": "#3498db"
    },
    73: {
        "title": "Twenty Thousand Leagues Under the Sea",
        "author": "Jules Verne",
        "genre": "Science Fiction",
        "year": 1870,
        "pages": 437,
        "summary": "Captain Nemo commands the submarine Nautilus on an underwater voyage of wonder and mystery. Verne's visionary adventure predicted modern submarines while exploring the depths of the ocean.",
        "read_link": "https://www.gutenberg.org/ebooks/164",
        "cover_color": "#0984e3"
    },
    74: {
        "title": "Journey to the Center of the Earth",
        "author": "Jules Verne",
        "genre": "Science Fiction",
        "year": 1864,
        "pages": 183,
        "summary": "Professor Lidenbrock leads an expedition into an Icelandic volcano to the Earth's core. Verne's imaginative adventure combines geological speculation with fantastic subterranean discoveries.",
        "read_link": "https://www.gutenberg.org/ebooks/18857",
        "cover_color": "#e74c3c"
    },
    75: {
        "title": "The Time Machine",
        "author": "H.G. Wells",
        "genre": "Science Fiction",
        "year": 1895,
        "pages": 118,
        "summary": "A scientist travels to the year 802,701 and discovers humanity's disturbing evolution. Wells' pioneering science fiction novel explores class division and the ultimate fate of civilization.",
        "read_link": "https://www.gutenberg.org/ebooks/35",
        "cover_color": "#6c5ce7"
    },
    76: {
        "title": "The War of the Worlds",
        "author": "H.G. Wells",
        "genre": "Science Fiction",
        "year": 1898,
        "pages": 192,
        "summary": "Martians invade Victorian England with terrifying war machines and heat-rays. The original alien invasion story that established templates for countless science fiction tales to follow.",
        "read_link": "https://www.gutenberg.org/ebooks/36",
        "cover_color": "#d63031"
    },
    77: {
        "title": "The Invisible Man",
        "author": "H.G. Wells",
        "genre": "Science Fiction",
        "year": 1897,
        "pages": 161,
        "summary": "A scientist discovers the secret of invisibility but cannot reverse it, descending into madness. Wells explores the corrupting nature of power and the isolation of the misunderstood genius.",
        "read_link": "https://www.gutenberg.org/ebooks/5230",
        "cover_color": "#2d3436"
    },
    78: {
        "title": "Slaughterhouse-Five",
        "author": "Kurt Vonnegut",
        "genre": "Science Fiction",
        "year": 1969,
        "pages": 275,
        "summary": "Billy Pilgrim becomes 'unstuck in time' after surviving the Dresden bombing and alien abduction. Vonnegut's anti-war masterpiece blends science fiction with profound meditation on trauma and fate.",
        "read_link": "https://www.amazon.com/Slaughterhouse-Five-Novel-Modern-Library-Novels/dp/0385333846",
        "cover_color": "#74b9ff"
    },
    79: {
        "title": "Cat's Cradle",
        "author": "Kurt Vonnegut",
        "genre": "Science Fiction",
        "year": 1963,
        "pages": 287,
        "summary": "A writer researching the atomic bomb discovers a substance that could freeze all water on Earth. Vonnegut's darkly comic satire explores science, religion, and humanity's capacity for self-destruction.",
        "read_link": "https://www.amazon.com/Cats-Cradle-Novel-Kurt-Vonnegut/dp/038533348X",
        "cover_color": "#00cec9"
    },
    80: {
        "title": "Catch-22",
        "author": "Joseph Heller",
        "genre": "Satire",
        "year": 1961,
        "pages": 453,
        "summary": "Bombardier Yossarian tries to escape military service during World War II through the absurd Catch-22. Heller's classic anti-war satire coined a term and captured the insanity of bureaucracy.",
        "read_link": "https://www.amazon.com/Catch-22-50th-Anniversary-Joseph-Heller/dp/1451626657",
        "cover_color": "#fdcb6e"
    },
    81: {
        "title": "Beloved",
        "author": "Toni Morrison",
        "genre": "Fiction",
        "year": 1987,
        "pages": 324,
        "summary": "Escaped slave Sethe is haunted by the ghost of her dead daughter in post-Civil War Ohio. Morrison's Pulitzer Prize winner explores the devastating psychological legacy of slavery with poetic power.",
        "read_link": "https://www.amazon.com/Beloved-Toni-Morrison/dp/1400033411",
        "cover_color": "#636e72"
    },
    82: {
        "title": "Song of Solomon",
        "author": "Toni Morrison",
        "genre": "Fiction",
        "year": 1977,
        "pages": 337,
        "summary": "Milkman Dead searches for a family treasure that leads him to discover his roots and identity. Morrison's lyrical novel weaves African American folklore with a young man's journey to selfhood.",
        "read_link": "https://www.amazon.com/Song-Solomon-Toni-Morrison/dp/140003342X",
        "cover_color": "#a29bfe"
    },
    83: {
        "title": "The Color Purple",
        "author": "Alice Walker",
        "genre": "Fiction",
        "year": 1982,
        "pages": 295,
        "summary": "Celie's letters reveal her transformation from abuse victim to self-empowered woman in the rural South. Walker's Pulitzer Prize winner celebrates the strength and resilience of Black women.",
        "read_link": "https://www.amazon.com/Color-Purple-Novel-Alice-Walker/dp/0156028352",
        "cover_color": "#9b59b6"
    },
    84: {
        "title": "Their Eyes Were Watching God",
        "author": "Zora Neale Hurston",
        "genre": "Fiction",
        "year": 1937,
        "pages": 219,
        "summary": "Janie Crawford's three marriages become a journey toward self-discovery and true love. A lyrical masterpiece of the Harlem Renaissance exploring Black female identity and independence.",
        "read_link": "https://www.amazon.com/Their-Eyes-Were-Watching-God/dp/0061120065",
        "cover_color": "#00b894"
    },
    85: {
        "title": "Invisible Man",
        "author": "Ralph Ellison",
        "genre": "Fiction",
        "year": 1952,
        "pages": 581,
        "summary": "An unnamed Black narrator describes his journey from the South to Harlem, invisible in American society. A landmark novel exploring race, identity, and the African American experience.",
        "read_link": "https://www.amazon.com/Invisible-Man-Ralph-Ellison/dp/0679732764",
        "cover_color": "#2d3436"
    },
    86: {
        "title": "Native Son",
        "author": "Richard Wright",
        "genre": "Fiction",
        "year": 1940,
        "pages": 504,
        "summary": "Bigger Thomas's desperate crime in 1930s Chicago exposes the devastating effects of racism. Wright's unflinching novel shocked America and changed the conversation about race in literature.",
        "read_link": "https://www.amazon.com/Native-Son-Perennial-Classics-Richard/dp/0060837569",
        "cover_color": "#e74c3c"
    },
    87: {
        "title": "The Sun Also Rises",
        "author": "Ernest Hemingway",
        "genre": "Fiction",
        "year": 1926,
        "pages": 251,
        "summary": "Disillusioned Americans and British expatriates drink and travel through 1920s Paris and Spain. Hemingway's debut novel captures the Lost Generation's search for meaning after World War I.",
        "read_link": "https://www.amazon.com/Sun-Also-Rises-Ernest-Hemingway/dp/0743297334",
        "cover_color": "#f39c12"
    },
    88: {
        "title": "A Farewell to Arms",
        "author": "Ernest Hemingway",
        "genre": "Fiction",
        "year": 1929,
        "pages": 332,
        "summary": "An American ambulance driver falls in love with a British nurse during World War I in Italy. Hemingway's semi-autobiographical novel combines war's brutality with tender, doomed romance.",
        "read_link": "https://www.amazon.com/Farewell-Arms-Ernest-Hemingway/dp/0684801469",
        "cover_color": "#636e72"
    },
    89: {
        "title": "The Old Man and the Sea",
        "author": "Ernest Hemingway",
        "genre": "Fiction",
        "year": 1952,
        "pages": 127,
        "summary": "An aging Cuban fisherman battles a giant marlin in the Gulf Stream for three days. Hemingway's Pulitzer Prize winner is a profound meditation on perseverance, dignity, and human spirit.",
        "read_link": "https://www.amazon.com/Old-Man-Sea-Ernest-Hemingway/dp/0684801221",
        "cover_color": "#0984e3"
    },
    90: {
        "title": "For Whom the Bell Tolls",
        "author": "Ernest Hemingway",
        "genre": "Fiction",
        "year": 1940,
        "pages": 471,
        "summary": "An American dynamiter joins Spanish guerrillas to blow up a bridge during the Civil War. Hemingway's epic tale of war, love, and sacrifice unfolds over three intense days in the mountains.",
        "read_link": "https://www.amazon.com/Whom-Bell-Tolls-Ernest-Hemingway/dp/0684803356",
        "cover_color": "#c0392b"
    },
    91: {
        "title": "One Flew Over the Cuckoo's Nest",
        "author": "Ken Kesey",
        "genre": "Fiction",
        "year": 1962,
        "pages": 325,
        "summary": "Randle McMurphy fakes insanity to serve his prison sentence in a mental hospital, challenging Nurse Ratched. A powerful allegory about conformity, rebellion, and the nature of sanity itself.",
        "read_link": "https://www.amazon.com/Flew-Over-Cuckoos-Nest-Novel/dp/0451163966",
        "cover_color": "#3498db"
    },
    92: {
        "title": "On the Road",
        "author": "Jack Kerouac",
        "genre": "Fiction",
        "year": 1957,
        "pages": 307,
        "summary": "Sal Paradise chronicles his wild road trips across America with the magnetic Dean Moriarty. The defining novel of the Beat Generation captures the restless quest for meaning and freedom.",
        "read_link": "https://www.amazon.com/Road-Original-Scroll-Penguin-Classics/dp/0143105469",
        "cover_color": "#f9ca24"
    },
    93: {
        "title": "The Grapes of Wrath",
        "author": "John Steinbeck",
        "genre": "Fiction",
        "year": 1939,
        "pages": 464,
        "summary": "The Joad family flees Oklahoma's Dust Bowl for California's promised land. Steinbeck's Pulitzer Prize winner is a searing portrait of American poverty and resilience during the Great Depression.",
        "read_link": "https://www.amazon.com/Grapes-Wrath-John-Steinbeck/dp/0143039431",
        "cover_color": "#e17055"
    },
    94: {
        "title": "Of Mice and Men",
        "author": "John Steinbeck",
        "genre": "Fiction",
        "year": 1937,
        "pages": 107,
        "summary": "Two migrant workers, George and gentle giant Lennie, dream of owning their own farm. A heartbreaking novella about friendship, dreams, and the harsh realities faced by society's outcasts.",
        "read_link": "https://www.amazon.com/Mice-Men-John-Steinbeck/dp/0140186425",
        "cover_color": "#636e72"
    },
    95: {
        "title": "East of Eden",
        "author": "John Steinbeck",
        "genre": "Fiction",
        "year": 1952,
        "pages": 601,
        "summary": "Two families' intertwined stories in California's Salinas Valley retell the Cain and Abel narrative. Steinbeck considered this his masterpiece—an epic exploration of good, evil, and free will.",
        "read_link": "https://www.amazon.com/East-Eden-John-Steinbeck/dp/0140186395",
        "cover_color": "#27ae60"
    },
    96: {
        "title": "Lolita",
        "author": "Vladimir Nabokov",
        "genre": "Fiction",
        "year": 1955,
        "pages": 336,
        "summary": "Humbert Humbert's disturbing obsession with young Dolores Haze, whom he calls Lolita. A controversial masterpiece of prose that explores the darkest corners of obsession and delusion.",
        "read_link": "https://www.amazon.com/Lolita-Vladimir-Nabokov/dp/0679723161",
        "cover_color": "#e84393"
    },
    97: {
        "title": "Pale Fire",
        "author": "Vladimir Nabokov",
        "genre": "Fiction",
        "year": 1962,
        "pages": 315,
        "summary": "A poem and its bizarre commentary reveal a story of madness, exile, and possible assassination. Nabokov's innovative novel plays with narrative structure in dazzling, unexpected ways.",
        "read_link": "https://www.amazon.com/Pale-Fire-Vladimir-Nabokov/dp/0679723420",
        "cover_color": "#dfe6e9"
    },
    98: {
        "title": "Midnight's Children",
        "author": "Salman Rushdie",
        "genre": "Fiction",
        "year": 1981,
        "pages": 533,
        "summary": "Children born at India's independence have magical powers in this Booker Prize winner. Rushdie's dazzling novel weaves personal and national history into magical realist epic.",
        "read_link": "https://www.amazon.com/Midnights-Children-Modern-Library-Novels/dp/0812976533",
        "cover_color": "#f39c12"
    },
    99: {
        "title": "One Hundred Years of Solitude",
        "author": "Gabriel García Márquez",
        "genre": "Fiction",
        "year": 1967,
        "pages": 417,
        "summary": "Seven generations of the Buendía family live in the mythical town of Macondo. García Márquez's masterpiece of magical realism explores love, war, and the cyclical nature of history.",
        "read_link": "https://www.amazon.com/Hundred-Solitude-Harper-Perennial-Classics/dp/0060883286",
        "cover_color": "#00b894"
    },
    100: {
        "title": "Love in the Time of Cholera",
        "author": "Gabriel García Márquez",
        "genre": "Romance",
        "year": 1985,
        "pages": 348,
        "summary": "Florentino Ariza waits fifty years to declare his love to Fermina Daza. A lush, sweeping romance that explores love in all its forms—obsessive, requited, and eternal.",
        "read_link": "https://www.amazon.com/Love-Time-Cholera-Gabriel-Garcia/dp/0307389731",
        "cover_color": "#e84393"
    }
}

def get_book_info(book_id):
    """Get book information by ID"""
    return BOOKS_DATABASE.get(book_id, None)

def get_all_books():
    """Get all books as a list"""
    return list(BOOKS_DATABASE.values())

def search_books(query):
    """Search books by title or author"""
    query = query.lower()
    results = []
    for book_id, book in BOOKS_DATABASE.items():
        if query in book['title'].lower() or query in book['author'].lower():
            results.append({**book, 'book_id': book_id})
    return results
