"""
Comprehensive book database with summaries and reading links
Links are to Open Library, Project Gutenberg, and other free reading resources
"""

BOOKS_DATABASE = {
    1: {
        "title": "Brave New World",
        "author": "Aldous Huxley",
        "genre": "Science Fiction",
        "year": 1932,
        "pages": 311,
        "summary": "A haunting vision of a future society where humans are genetically engineered and conditioned to be content with their lot. Explores themes of technology, control, and the cost of happiness in a world without pain or struggle.",
        "read_link": "https://openlibrary.org/works/OL64440W/Brave_New_World",
        "cover_color": "#1a1a2e"
    },
    2: {
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "year": 1954,
        "pages": 1178,
        "summary": "An epic tale of good versus evil in the magical realm of Middle-earth. Follow Frodo Baggins and his fellowship on their perilous quest to destroy the One Ring and save their world from the Dark Lord Sauron.",
        "read_link": "https://openlibrary.org/works/OL27448W/The_Lord_of_the_Rings?edition=key:/books/OL51711484M",
        "cover_color": "#2d3436"
    },
    3: {
        "title": "Paper Towns",
        "author": "John Green",
        "genre": "Young Adult",
        "year": 2008,
        "pages": 305,
        "summary": "A captivating mystery about Quentin's journey to find his enigmatic neighbor Margo Roth Spiegelman after she disappears. A thoughtful exploration of identity, perception, and the danger of idealizing people.",
        "read_link": "https://openlibrary.org/works/OL11822690W/Paper_towns?edition=key%3A/books/OL31880481M",
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
        "read_link": "https://openlibrary.org/works/OL6027236W/The_Maze_Runner?edition=key%3A/books/OL23147747M",
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
        "read_link": "https://openlibrary.org/works/OL82592W/Harry_Potter_and_the_Sorcerers_Stone",
        "cover_color": "#e17055"
    },
    8: {
        "title": "The Handmaid's Tale",
        "author": "Margaret Atwood",
        "genre": "Dystopian",
        "year": 1985,
        "pages": 311,
        "summary": "In the totalitarian Republic of Gilead, Offred serves as a handmaid forced to bear children. A chilling portrayal of women's oppression and a powerful warning about religious extremism and authoritarian control.",
        "read_link": "https://openlibrary.org/works/OL675783W/The_Handmaid's_Tale?edition=key:/books/OL51647052M",
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
        "read_link": "https://openlibrary.org/works/OL16239762W/Gone_Girl?edition=key:/books/OL35889560M",
        "cover_color": "#2d3436"
    },
    11: {
        "title": "Fahrenheit 451",
        "author": "Ray Bradbury",
        "genre": "Science Fiction",
        "year": 1953,
        "pages": 158,
        "summary": "In a future where books are banned and burned, fireman Guy Montag begins to question everything. A powerful warning about censorship, conformity, and the importance of critical thinking in society.",
        "read_link": "https://openlibrary.org/works/OL103123W/Fahrenheit_451?edition=key:/books/OL49213952M",
        "cover_color": "#e74c3c"
    },
    12: {
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "year": 1949,
        "pages": 328,
        "summary": "Winston Smith lives in a totalitarian state where Big Brother watches everything. A haunting exploration of surveillance, propaganda, and thought control that remains disturbingly relevant today.",
        "read_link": "https://openlibrary.org/works/OL1168083W/Nineteen_Eighty-Four",
        "cover_color": "#2c3e50"
    },
    13: {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "year": 1813,
        "pages": 279,
        "summary": "Elizabeth Bennet and Mr. Darcy navigate class, manners, and misconceptions in Regency England. A witty romantic masterpiece that brilliantly explores love, pride, and the art of changing one's first impressions.",
        "read_link": "https://www.gutenberg.org/ebooks/1342",
        "cover_color": "#fd79a8"
    },
    14: {
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
        "genre": "Dystopian",
        "year": 2008,
        "pages": 374,
        "summary": "In a dystopian future, Katniss Everdeen volunteers to take her sister's place in a televised death match. A gripping tale of survival, rebellion, and the human cost of entertainment and political control.",
        "read_link": "https://openlibrary.org/works/OL5735363W/The_Hunger_Games?edition=key%3A/books/OL46874697M",
        "cover_color": "#e74c3c"
    },
    15: {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Fiction",
        "year": 1960,
        "pages": 281,
        "summary": "Scout Finch watches her father Atticus defend a Black man accused of rape in 1930s Alabama. A profound exploration of racial injustice, moral courage, and the loss of innocence that shaped American literature.",
        "read_link": "https://openlibrary.org/works/OL3140822W/To_Kill_a_Mockingbird?edition=key:/books/OL25228947M",
        "cover_color": "#00cec9"
    },
    16: {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Fiction",
        "year": 1951,
        "pages": 234,
        "summary": "Holden Caulfield narrates his experiences in New York City after being expelled from prep school. A landmark novel capturing teenage alienation, rebellion, and the painful transition to adulthood.",
        "read_link": "https://openlibrary.org/works/OL3335245W/The_Catcher_in_the_Rye?edition=key:/books/OL50512910M",
        "cover_color": "#d63031"
    },
    17: {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "genre": "Fiction",
        "year": 1988,
        "pages": 208,
        "summary": "Santiago, a shepherd boy, embarks on a journey to find treasure at the Egyptian pyramids. A mystical fable about following your dreams, listening to your heart, and discovering your personal legend.",
        "read_link": "https://openlibrary.org/works/OL796465W/O_Alquimista?edition=key%3A/books/OL7288233M",
        "cover_color": "#fdcb6e"
    },
    18: {
        "title": "Dune",
        "author": "Frank Herbert",
        "genre": "Science Fiction",
        "year": 1965,
        "pages": 688,
        "summary": "Paul Atreides is thrust into a world of political intrigue on the desert planet Arrakis. An epic saga of power, religion, and ecology that redefined science fiction and influenced generations of storytelling.",
        "read_link": "https://openlibrary.org/works/OL893415W/Dune",
        "cover_color": "#d35400"
    },
    19: {
        "title": "The Da Vinci Code",
        "author": "Dan Brown",
        "genre": "Thriller",
        "year": 2003,
        "pages": 454,
        "summary": "Robert Langdon unravels a murder mystery in the Louvre that leads to secrets hidden for centuries. A fast-paced thriller combining art history, religious mysteries, and code-breaking that captivated millions.",
        "read_link": "https://openlibrary.org/works/OL76837W/The_Da_Vinci_Code?edition=key:/books/OL35696920M",
        "cover_color": "#8e44ad"
    },
    20: {
        "title": "The Shining",
        "author": "Stephen King",
        "genre": "Horror",
        "year": 1977,
        "pages": 447,
        "summary": "Jack Torrance takes a job as winter caretaker at the isolated Overlook Hotel with his family. A terrifying descent into madness as supernatural forces exploit Jack's demons and threaten his young son Danny.",
        "read_link": "https://openlibrary.org/works/OL81633W/The_Shining?edition=key:/books/OL10631997M",
        "cover_color": "#2d3436"
    },
    21: {
        "title": "Jane Eyre",
        "author": "Charlotte Bronte",
        "genre": "Romance",
        "year": 1847,
        "pages": 500,
        "summary": "Orphaned Jane becomes governess at Thornfield Hall and falls for the mysterious Mr. Rochester. A groundbreaking novel of female independence, moral integrity, and passionate love that defied Victorian conventions.",
        "read_link": "https://www.gutenberg.org/ebooks/1260",
        "cover_color": "#6c5ce7"
    },
    22: {
        "title": "Dracula",
        "author": "Bram Stoker",
        "genre": "Horror",
        "year": 1897,
        "pages": 418,
        "summary": "Jonathan Harker's visit to Count Dracula's castle in Transylvania unleashes ancient evil on England. The definitive vampire novel that created modern horror and still chills readers over a century later.",
        "read_link": "https://www.gutenberg.org/ebooks/345",
        "cover_color": "#c0392b"
    },
    23: {
        "title": "Frankenstein",
        "author": "Mary Shelley",
        "genre": "Horror",
        "year": 1818,
        "pages": 280,
        "summary": "Victor Frankenstein creates life but abandons his creation, leading to tragic consequences. A profound meditation on scientific responsibility, loneliness, and what it means to be human that birthed science fiction.",
        "read_link": "https://www.gutenberg.org/ebooks/84",
        "cover_color": "#27ae60"
    },
    24: {
        "title": "Wuthering Heights",
        "author": "Emily Bronte",
        "genre": "Romance",
        "year": 1847,
        "pages": 416,
        "summary": "The passionate and destructive love between Heathcliff and Catherine haunts the Yorkshire moors. A dark, intense tale of obsession, revenge, and love that transcends death, defying romantic conventions.",
        "read_link": "https://www.gutenberg.org/ebooks/768",
        "cover_color": "#8e44ad"
    },
    25: {
        "title": "The Picture of Dorian Gray",
        "author": "Oscar Wilde",
        "genre": "Fiction",
        "year": 1890,
        "pages": 254,
        "summary": "Dorian Gray remains eternally young while his portrait ages and shows his sins. Wilde's only novel is a witty, dark exploration of beauty, corruption, and the price of pursuing pleasure without consequence.",
        "read_link": "https://www.gutenberg.org/ebooks/174",
        "cover_color": "#9b59b6"
    },
    26: {
        "title": "Moby Dick",
        "author": "Herman Melville",
        "genre": "Fiction",
        "year": 1851,
        "pages": 635,
        "summary": "Captain Ahab obsessively hunts the white whale that took his leg across the world's oceans. An ambitious epic exploring obsession, nature, fate, and the limits of human understanding that redefined American literature.",
        "read_link": "https://www.gutenberg.org/ebooks/2701",
        "cover_color": "#3498db"
    },
    27: {
        "title": "The Adventures of Sherlock Holmes",
        "author": "Arthur Conan Doyle",
        "genre": "Mystery",
        "year": 1892,
        "pages": 307,
        "summary": "Follow the brilliant detective Sherlock Holmes and Dr. Watson through twelve captivating cases. The definitive collection that established Holmes as literature's greatest detective and mystery fiction's gold standard.",
        "read_link": "https://www.gutenberg.org/ebooks/1661",
        "cover_color": "#2c3e50"
    },
    28: {
        "title": "The Count of Monte Cristo",
        "author": "Alexandre Dumas",
        "genre": "Adventure",
        "year": 1844,
        "pages": 1276,
        "summary": "Edmond Dantes, wrongly imprisoned, escapes and reinvents himself to exact revenge on those who betrayed him. An unforgettable tale of vengeance, justice, and redemption that remains the ultimate adventure classic.",
        "read_link": "https://www.gutenberg.org/ebooks/1184",
        "cover_color": "#2980b9"
    },
    29: {
        "title": "A Tale of Two Cities",
        "author": "Charles Dickens",
        "genre": "Historical Fiction",
        "year": 1859,
        "pages": 448,
        "summary": "London and Paris during the French Revolution form the backdrop for this tale of sacrifice and resurrection. Dickens weaves love, loyalty, and redemption through one of history's most turbulent periods.",
        "read_link": "https://www.gutenberg.org/ebooks/98",
        "cover_color": "#e74c3c"
    },
    30: {
        "title": "Great Expectations",
        "author": "Charles Dickens",
        "genre": "Fiction",
        "year": 1861,
        "pages": 544,
        "summary": "Orphan Pip's life changes when a mysterious benefactor funds his rise to gentleman status. A masterful coming-of-age story exploring class, ambition, and the true meaning of wealth and gentility.",
        "read_link": "https://www.gutenberg.org/ebooks/1400",
        "cover_color": "#795548"
    },
    31: {
        "title": "The Odyssey",
        "author": "Homer",
        "genre": "Fiction",
        "year": -800,
        "pages": 374,
        "summary": "Odysseus struggles to return home after the Trojan War, facing monsters, gods, and temptations. The foundational adventure story that has influenced literature for nearly three thousand years.",
        "read_link": "https://www.gutenberg.org/ebooks/1727",
        "cover_color": "#16a085"
    },
    32: {
        "title": "The Iliad",
        "author": "Homer",
        "genre": "Fiction",
        "year": -750,
        "pages": 704,
        "summary": "The Greek siege of Troy comes alive through the wrath of Achilles and the heroes' struggle. The epic poem that defined Western literature and shaped our understanding of war, honor, and mortality.",
        "read_link": "https://www.gutenberg.org/ebooks/6130",
        "cover_color": "#c0392b"
    },
    33: {
        "title": "Don Quixote",
        "author": "Miguel de Cervantes",
        "genre": "Fiction",
        "year": 1605,
        "pages": 1056,
        "summary": "An aging gentleman believes he's a knight and sets out on absurd adventures with his squire Sancho Panza. The first modern novel, a hilarious and touching exploration of idealism, reality, and the power of stories.",
        "read_link": "https://www.gutenberg.org/ebooks/996",
        "cover_color": "#d35400"
    },
    34: {
        "title": "Les Miserables",
        "author": "Victor Hugo",
        "genre": "Historical Fiction",
        "year": 1862,
        "pages": 1463,
        "summary": "Jean Valjean's journey from convict to saint in 19th century France, pursued by the relentless Javert. An epic of redemption, justice, and revolution that captures the full range of human experience.",
        "read_link": "https://www.gutenberg.org/ebooks/135",
        "cover_color": "#2c3e50"
    },
    35: {
        "title": "Anna Karenina",
        "author": "Leo Tolstoy",
        "genre": "Romance",
        "year": 1877,
        "pages": 864,
        "summary": "Anna's passionate affair with Count Vronsky unravels her marriage and her life in Tsarist Russia. Tolstoy's exploration of love, family, and society remains one of literature's greatest achievements.",
        "read_link": "https://www.gutenberg.org/ebooks/1399",
        "cover_color": "#e91e63"
    },
    36: {
        "title": "The Brothers Karamazov",
        "author": "Fyodor Dostoevsky",
        "genre": "Psychological Fiction",
        "year": 1880,
        "pages": 796,
        "summary": "Three brothers grapple with faith, morality, and patricide in this profound philosophical novel. Dostoevsky's masterpiece explores the eternal questions of God, freedom, and the nature of evil.",
        "read_link": "https://www.gutenberg.org/ebooks/28054",
        "cover_color": "#6c5ce7"
    },
    37: {
        "title": "The Scarlet Letter",
        "author": "Nathaniel Hawthorne",
        "genre": "Fiction",
        "year": 1850,
        "pages": 272,
        "summary": "Hester Prynne wears the mark of adultery in Puritan Boston while hiding her lover's identity. A powerful exploration of sin, guilt, and redemption that questions rigid moral codes and social punishment.",
        "read_link": "https://www.gutenberg.org/ebooks/25344",
        "cover_color": "#e74c3c"
    },
    38: {
        "title": "The Divine Comedy",
        "author": "Dante Alighieri",
        "genre": "Poetry",
        "year": 1320,
        "pages": 798,
        "summary": "Dante journeys through Hell, Purgatory, and Paradise guided by Virgil and Beatrice. The supreme achievement of medieval literature, blending theology, philosophy, and poetry into an unforgettable vision.",
        "read_link": "https://www.gutenberg.org/ebooks/8800",
        "cover_color": "#9b59b6"
    },
    39: {
        "title": "The Grapes of Wrath",
        "author": "John Steinbeck",
        "genre": "Fiction",
        "year": 1939,
        "pages": 464,
        "summary": "The Joad family flees the Oklahoma Dust Bowl seeking a better life in California. Steinbeck's Pulitzer Prize winner is a devastating portrait of poverty, dignity, and the American Dream's failure.",
        "read_link": "https://openlibrary.org/works/OL23205W/The_Grapes_of_Wrath?edition=key:/books/OL58633642M",
        "cover_color": "#d35400"
    },
    40: {
        "title": "Of Mice and Men",
        "author": "John Steinbeck",
        "genre": "Fiction",
        "year": 1937,
        "pages": 107,
        "summary": "George and Lennie, two displaced migrant workers, dream of owning their own land. A heartbreaking novella about friendship, dreams, and the cruelty of circumstance during the Great Depression.",
        "read_link": "https://openlibrary.org/works/OL23204W/Of_Mice_and_Men?edition=key:/books/OL10159930M",
        "cover_color": "#795548"
    },
    41: {
        "title": "Lord of the Flies",
        "author": "William Golding",
        "genre": "Fiction",
        "year": 1954,
        "pages": 224,
        "summary": "British schoolboys stranded on an island descend into savagery without adult supervision. A disturbing allegory about civilization's fragility and the darkness lurking within human nature.",
        "read_link": "https://openlibrary.org/works/OL455327W/Lord_of_the_Flies?edition=key:/books/OL43025675M",
        "cover_color": "#27ae60"
    },
    42: {
        "title": "One Hundred Years of Solitude",
        "author": "Gabriel Garcia Marquez",
        "genre": "Fiction",
        "year": 1967,
        "pages": 417,
        "summary": "Seven generations of the Buendia family in the mythical town of Macondo live, love, and die. The masterpiece of magical realism blends history, fantasy, and family saga into an unforgettable tapestry.",
        "read_link": "https://openlibrary.org/works/OL274505W/Cien_a%C3%B1os_de_soledad?edition=key:/books/OL30448691M",
        "cover_color": "#f1c40f"
    },
    43: {
        "title": "Catch-22",
        "author": "Joseph Heller",
        "genre": "Fiction",
        "year": 1961,
        "pages": 453,
        "summary": "Bombardier Yossarian tries to survive World War II's absurdity while trapped by a maddening rule. A darkly comic satire of war, bureaucracy, and the insanity of trying to stay sane in an insane world.",
        "read_link": "https://openlibrary.org/works/OL276798W/Catch-22?edition=key:/books/OL20021159M",
        "cover_color": "#2980b9"
    },
    44: {
        "title": "Slaughterhouse-Five",
        "author": "Kurt Vonnegut",
        "genre": "Science Fiction",
        "year": 1969,
        "pages": 275,
        "summary": "Billy Pilgrim becomes unstuck in time, experiencing moments of his life randomly, including the Dresden bombing. A revolutionary anti-war novel blending science fiction with devastating memoir.",
        "read_link": "https://openlibrary.org/works/OL98459W/Slaughterhouse-Five?edition=key:/books/OL32142391M",
        "cover_color": "#00bcd4"
    },
    45: {
        "title": "The Bell Jar",
        "author": "Sylvia Plath",
        "genre": "Fiction",
        "year": 1963,
        "pages": 288,
        "summary": "Esther Greenwood's descent into depression during a New York summer internship. Plath's only novel is a haunting, semi-autobiographical exploration of mental illness, identity, and women's limited choices.",
        "read_link": "https://openlibrary.org/works/OL1865528W/The_Bell_Jar?edition=key%3A/books/OL37937797M",
        "cover_color": "#9c27b0"
    },
    46: {
        "title": "The Stranger",
        "author": "Albert Camus",
        "genre": "Philosophical Fiction",
        "year": 1942,
        "pages": 123,
        "summary": "Meursault commits a senseless murder and faces trial more for his emotional detachment than his crime. A landmark existentialist novel exploring absurdity, alienation, and society's need for conventional feelings.",
        "read_link": "https://openlibrary.org/works/OL1230613W/L%E2%80%99%C3%A9tranger?edition=key:/books/OL50985609M",
        "cover_color": "#607d8b"
    },
    47: {
        "title": "The Metamorphosis",
        "author": "Franz Kafka",
        "genre": "Fiction",
        "year": 1915,
        "pages": 201,
        "summary": "Gregor Samsa wakes one morning to find himself transformed into a giant insect. Kafka's masterpiece of alienation explores family, identity, and the horror of becoming unbearable to those who should love us.",
        "read_link": "https://openlibrary.org/works/OL498556W/Die_Verwandlung?edition=key:/books/OL24506210M",
        "cover_color": "#795548"
    },
    48: {
        "title": "Heart of Darkness",
        "author": "Joseph Conrad",
        "genre": "Fiction",
        "year": 1899,
        "pages": 96,
        "summary": "Marlow journeys up the Congo River to find the mysterious Kurtz, confronting colonialism's horror. A profound meditation on imperialism, morality, and the darkness within civilization itself.",
        "read_link": "https://www.gutenberg.org/ebooks/219",
        "cover_color": "#2c3e50"
    },
    49: {
        "title": "Beloved",
        "author": "Toni Morrison",
        "genre": "Fiction",
        "year": 1987,
        "pages": 324,
        "summary": "Former slave Sethe is haunted by the ghost of her dead daughter in post-Civil War Ohio. Morrison's Pulitzer Prize winner confronts slavery's psychological trauma with devastating power and beauty.",
        "read_link": "https://openlibrary.org/works/OL50548W/Beloved?edition=key%3A/books/OL48111094M",
        "cover_color": "#8e44ad"
    },
    50: {
        "title": "The Color Purple",
        "author": "Alice Walker",
        "genre": "Fiction",
        "year": 1982,
        "pages": 295,
        "summary": "Celie survives abuse and finds her voice through letters to God and her sister in rural Georgia. A powerful, uplifting novel of Black women's resilience, sisterhood, and the journey to self-discovery.",
        "read_link": "https://openlibrary.org/works/OL273644W/The_Color_Purple?edition=key:/books/OL54209038M",
        "cover_color": "#9c27b0"
    },
    51: {
        "title": "The Kite Runner",
        "author": "Khaled Hosseini",
        "genre": "Fiction",
        "year": 2003,
        "pages": 371,
        "summary": "Amir returns to Taliban-controlled Afghanistan to rescue the son of his childhood friend Hassan. A moving story of guilt, redemption, and the lasting impact of choices made in childhood.",
        "read_link": "https://openlibrary.org/works/OL5781992W/The_Kite_Runner?edition=key%3A/books/OL57895812M",
        "cover_color": "#f44336"
    },
    52: {
        "title": "Life of Pi",
        "author": "Yann Martel",
        "genre": "Fiction",
        "year": 2001,
        "pages": 319,
        "summary": "Pi Patel survives 227 days in a lifeboat with a Bengal tiger after a shipwreck. A captivating adventure that explores faith, storytelling, and the nature of truth through an extraordinary survival tale.",
        "read_link": "https://openlibrary.org/works/OL2827199W/Life_of_Pi?edition=key:/books/OL24636516M",
        "cover_color": "#03a9f4"
    },
    53: {
        "title": "The Book Thief",
        "author": "Markus Zusak",
        "genre": "Historical Fiction",
        "year": 2005,
        "pages": 552,
        "summary": "Death narrates the story of Liesel, a girl who steals books in Nazi Germany. A unique, heartbreaking tale of words, love, and survival during history's darkest chapter.",
        "read_link": "https://openlibrary.org/works/OL5819456W/The_Book_Thief?edition=key%3A/books/OL32840838M",
        "cover_color": "#424242"
    },
    54: {
        "title": "A Clockwork Orange",
        "author": "Anthony Burgess",
        "genre": "Dystopian",
        "year": 1962,
        "pages": 192,
        "summary": "Alex leads his gang through ultraviolence until the state tries to cure him of free will. A disturbing exploration of choice, morality, and whether forced goodness has any value at all.",
        "read_link": "https://openlibrary.org/works/OL261794W/A_Clockwork_Orange?edition=key:/books/OL27284158M",
        "cover_color": "#ff5722"
    },
    55: {
        "title": "The Road",
        "author": "Cormac McCarthy",
        "genre": "Post-Apocalyptic",
        "year": 2006,
        "pages": 287,
        "summary": "A father and son push a shopping cart through a devastated America, seeking survival. McCarthy's Pulitzer winner is a harrowing yet tender exploration of love and hope in a world without hope.",
        "read_link": "https://openlibrary.org/works/OL40873W/The_Road?edition=key%3A/books/OL32029168M",
        "cover_color": "#616161"
    },
    56: {
        "title": "Blood Meridian",
        "author": "Cormac McCarthy",
        "genre": "Western",
        "year": 1985,
        "pages": 351,
        "summary": "The Kid joins a gang of scalp hunters in the brutal American-Mexican borderlands of the 1850s. McCarthy's masterpiece of violence explores war, evil, and humanity's darkest nature in unflinching prose.",
        "read_link": "https://openlibrary.org/works/OL40879W/Blood_Meridian?edition=key:/books/OL48660197M",
        "cover_color": "#b71c1c"
    },
    57: {
        "title": "No Country for Old Men",
        "author": "Cormac McCarthy",
        "genre": "Thriller",
        "year": 2005,
        "pages": 309,
        "summary": "Llewelyn Moss finds drug money and triggers a chase with unstoppable killer Anton Chigurh. A taut thriller meditating on fate, violence, and a world where old values no longer apply.",
        "read_link": "https://openlibrary.org/works/OL40875W/No_country_for_old_men?edition=key:/books/OL3311863M",
        "cover_color": "#263238"
    },
    58: {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "year": 1937,
        "pages": 310,
        "summary": "Bilbo Baggins leaves the Shire for an unexpected adventure with dwarves seeking dragon treasure. The beloved prelude to Lord of the Rings that launched modern fantasy literature.",
        "read_link": "https://openlibrary.org/works/OL27482W/The_Hobbit?edition=key:/books/OL51709286M",
        "cover_color": "#4caf50"
    },
    59: {
        "title": "The Chronicles of Narnia",
        "author": "C.S. Lewis",
        "genre": "Fantasy",
        "year": 1950,
        "pages": 767,
        "summary": "Four children discover a magical land through a wardrobe and help the lion Aslan defeat evil. Lewis's beloved series blends adventure, allegory, and wonder into timeless children's fantasy.",
        "read_link": "https://openlibrary.org/works/OL70988W/The_Chronicles_of_Narnia?edition=key:/books/OL7542847M",
        "cover_color": "#2196f3"
    },
    60: {
        "title": "Ender's Game",
        "author": "Orson Scott Card",
        "genre": "Science Fiction",
        "year": 1985,
        "pages": 324,
        "summary": "Child genius Ender Wiggin is trained in Battle School to fight an alien threat to humanity. A gripping tale of strategy, leadership, and the moral costs of warfare that transcends its genre.",
        "read_link": "https://openlibrary.org/works/OL49488W/Ender's_Game?edition=key:/books/OL43190630M",
        "cover_color": "#00bcd4"
    },
    61: {
        "title": "The Hitchhiker's Guide to the Galaxy",
        "author": "Douglas Adams",
        "genre": "Science Fiction",
        "year": 1979,
        "pages": 193,
        "summary": "Arthur Dent escapes Earth's destruction and hitchhikes through the galaxy with his alien friend. A hilarious cosmic adventure that answers why the number 42 is so important.",
        "read_link": "https://openlibrary.org/works/OL2163649W/The_Hitch_Hiker's_Guide_to_the_Galaxy?edition=key:/books/OL32832539M",
        "cover_color": "#009688"
    },
    62: {
        "title": "Foundation",
        "author": "Isaac Asimov",
        "genre": "Science Fiction",
        "year": 1951,
        "pages": 244,
        "summary": "Mathematician Hari Seldon predicts the fall of the Galactic Empire and creates a plan to shorten the dark age. Asimov's epic explores the power of science and knowledge to shape civilization's future.",
        "read_link": "https://openlibrary.org/works/OL46125W/Foundation?edition=key:/books/OL51566464M",
        "cover_color": "#673ab7"
    },
    63: {
        "title": "Neuromancer",
        "author": "William Gibson",
        "genre": "Science Fiction",
        "year": 1984,
        "pages": 271,
        "summary": "Washed-up hacker Case gets one last chance at the computer networks that are his life. The novel that defined cyberpunk and predicted our digital future with uncanny prescience.",
        "read_link": "https://openlibrary.org/works/OL27258W/Neuromancer?edition=key:/books/OL27444262M",
        "cover_color": "#00e676"
    },
    64: {
        "title": "Snow Crash",
        "author": "Neal Stephenson",
        "genre": "Science Fiction",
        "year": 1992,
        "pages": 440,
        "summary": "Hiro Protagonist, pizza deliverer and hacker, investigates a new drug that crashes both computers and minds. A wild ride through virtual reality and linguistics that foresaw the metaverse.",
        "read_link": "https://openlibrary.org/works/OL38501W/Snow_Crash?edition=key:/books/OL14813122M",
        "cover_color": "#00bcd4"
    },
    65: {
        "title": "The Martian",
        "author": "Andy Weir",
        "genre": "Science Fiction",
        "year": 2011,
        "pages": 369,
        "summary": "Astronaut Mark Watney is stranded alone on Mars and must science his way to survival. A gripping, scientifically accurate survival story with humor, ingenuity, and unstoppable human determination.",
        "read_link": "https://openlibrary.org/works/OL17091839W/The_Martian?edition=key%3A/books/OL32815550M",
        "cover_color": "#ff5722"
    },
    66: {
        "title": "Ready Player One",
        "author": "Ernest Cline",
        "genre": "Science Fiction",
        "year": 2011,
        "pages": 374,
        "summary": "In 2045, Wade Watts hunts for a hidden Easter egg in a virtual reality universe that could make him rich. A nostalgic adventure through 1980s pop culture and gaming that celebrates geek culture.",
        "read_link": "https://openlibrary.org/works/OL15936512W/Ready_Player_One?edition=key:/books/OL27257671M",
        "cover_color": "#e91e63"
    },
    67: {
        "title": "It",
        "author": "Stephen King",
        "genre": "Horror",
        "year": 1986,
        "pages": 1138,
        "summary": "Seven friends reunite to fight the evil entity that haunted their childhood in Derry, Maine. King's epic horror novel explores the power of memory, friendship, and facing our deepest fears.",
        "read_link": "https://openlibrary.org/works/OL81613W/It?edition=key%3A/books/OL7572658M",
        "cover_color": "#f44336"
    },
    68: {
        "title": "Pet Sematary",
        "author": "Stephen King",
        "genre": "Horror",
        "year": 1983,
        "pages": 374,
        "summary": "A family discovers a burial ground that brings the dead back to life, but not as they were. King's most terrifying novel explores grief, death, and the terrible price of defying nature's laws.",
        "read_link": "https://openlibrary.org/works/OL81631W/Pet_Sematary?edition=key:/books/OL7572262M",
        "cover_color": "#424242"
    },
    69: {
        "title": "The Stand",
        "author": "Stephen King",
        "genre": "Post-Apocalyptic",
        "year": 1978,
        "pages": 1153,
        "summary": "A deadly plague wipes out most of humanity, and survivors must choose between good and evil. King's epic masterpiece of apocalyptic fiction explores the eternal battle for humanity's soul.",
        "read_link": "https://openlibrary.org/works/OL81618W/The_Stand?edition=key%3A/books/OL58142869M",
        "cover_color": "#2c3e50"
    },
    70: {
        "title": "American Gods",
        "author": "Neil Gaiman",
        "genre": "Fantasy",
        "year": 2001,
        "pages": 465,
        "summary": "Shadow Moon joins the mysterious Mr. Wednesday on a road trip across America's mythological landscape. Gaiman's epic blends Norse mythology with American folklore in a battle of old and new gods.",
        "read_link": "https://openlibrary.org/works/OL679360W/American_Gods?edition=key:/books/OL32582534M",
        "cover_color": "#3f51b5"
    },
    71: {
        "title": "Good Omens",
        "author": "Neil Gaiman & Terry Pratchett",
        "genre": "Fantasy",
        "year": 1990,
        "pages": 400,
        "summary": "An angel and demon team up to prevent the apocalypse because they've grown fond of Earth. A hilarious, warm-hearted comedy about friendship, free will, and the end of the world.",
        "read_link": "https://openlibrary.org/works/OL453936W/Good_Omens?edition=key:/books/OL24084500M",
        "cover_color": "#ffc107"
    },
    72: {
        "title": "The Name of the Wind",
        "author": "Patrick Rothfuss",
        "genre": "Fantasy",
        "year": 2007,
        "pages": 662,
        "summary": "Kvothe, a legendary figure, tells his own story from orphan to hero to broken innkeeper. A beautifully written fantasy about the power of stories, music, and the making of myths.",
        "read_link": "https://openlibrary.org/works/OL8479867W/The_Name_of_the_Wind?edition=key:/books/OL35447857M",
        "cover_color": "#ff9800"
    },
    73: {
        "title": "The Way of Kings",
        "author": "Brandon Sanderson",
        "genre": "Fantasy",
        "year": 2010,
        "pages": 1007,
        "summary": "On a world of storms and strange magic, heroes emerge to face an ancient evil returning. Sanderson's epic begins a massive fantasy series with intricate magic systems and complex characters.",
        "read_link": "https://openlibrary.org/works/OL15358691W/The_Way_of_Kings?edition=key:/books/OL24383834M",
        "cover_color": "#2196f3"
    },
    74: {
        "title": "A Game of Thrones",
        "author": "George R.R. Martin",
        "genre": "Fantasy",
        "year": 1996,
        "pages": 694,
        "summary": "Noble families vie for the Iron Throne while an ancient threat stirs in the frozen north. Martin's epic fantasy redefined the genre with its moral complexity, political intrigue, and shocking twists.",
        "read_link": "https://openlibrary.org/works/OL257943W/A_Game_of_Thrones?edition=key:/books/OL58636603M",
        "cover_color": "#b71c1c"
    },
    75: {
        "title": "The Night Circus",
        "author": "Erin Morgenstern",
        "genre": "Fantasy",
        "year": 2011,
        "pages": 387,
        "summary": "Two young magicians are bound in a competition using a mysterious black and white circus as their arena. A dreamy, romantic fantasy with enchanting prose and unforgettable atmosphere.",
        "read_link": "https://openlibrary.org/works/OL16086747W/The_Night_Circus?edition=key:/books/OL33390399M",
        "cover_color": "#212121"
    },
    76: {
        "title": "The Girl with the Dragon Tattoo",
        "author": "Stieg Larsson",
        "genre": "Thriller",
        "year": 2005,
        "pages": 465,
        "summary": "Journalist Mikael Blomkvist and hacker Lisbeth Salander investigate a decades-old disappearance. A gripping Swedish thriller combining mystery, family secrets, and unforgettable characters.",
        "read_link": "https://openlibrary.org/works/OL5784622W/M%C3%A4n_som_hatar_kvinnor?edition=key:/books/OL58852921M",
        "cover_color": "#455a64"
    },
    77: {
        "title": "The Girl on the Train",
        "author": "Paula Hawkins",
        "genre": "Thriller",
        "year": 2015,
        "pages": 323,
        "summary": "Rachel watches a perfect couple from her train window until she sees something that changes everything. A twisty psychological thriller about obsession, memory, and the lies we tell ourselves.",
        "read_link": "https://openlibrary.org/works/OL17112428W/The_Girl_on_the_Train?edition=key:/books/OL28597980M",
        "cover_color": "#37474f"
    },
    78: {
        "title": "Big Little Lies",
        "author": "Liane Moriarty",
        "genre": "Thriller",
        "year": 2014,
        "pages": 460,
        "summary": "Three mothers' lives intersect at a school trivia night that ends in death. A darkly funny mystery about the secrets behind perfect suburban facades and the violence they can hide.",
        "read_link": "https://openlibrary.org/works/OL17116911W/Big_Little_Lies?edition=key:/books/OL28234618M",
        "cover_color": "#e91e63"
    },
    79: {
        "title": "The Silent Patient",
        "author": "Alex Michaelides",
        "genre": "Thriller",
        "year": 2019,
        "pages": 325,
        "summary": "Alicia Berenson shot her husband and hasn't spoken since. Therapist Theo Faber is determined to uncover why. A twisted psychological thriller with a shocking ending you won't see coming.",
        "read_link": "https://openlibrary.org/works/OL19096402W/The_Silent_Patient?edition=key:/books/OL59645497M",
        "cover_color": "#263238"
    },
    80: {
        "title": "Where the Crawdads Sing",
        "author": "Delia Owens",
        "genre": "Fiction",
        "year": 2018,
        "pages": 368,
        "summary": "Kya, the 'Marsh Girl,' grows up alone in the North Carolina wetlands and becomes a murder suspect. A beautiful blend of mystery, coming-of-age, and nature writing that captivated millions.",
        "read_link": "https://openlibrary.org/works/OL18766691W/Where_the_Crawdads_Sing?edition=key:/books/OL26974769M",
        "cover_color": "#4caf50"
    },
    81: {
        "title": "Educated",
        "author": "Tara Westover",
        "genre": "Memoir",
        "year": 2018,
        "pages": 334,
        "summary": "Tara grows up in a survivalist family in Idaho with no formal education until she teaches herself to attend college. A remarkable memoir of self-invention and escaping a violent, isolated upbringing.",
        "read_link": "https://openlibrary.org/works/OL18139176W/Educated",
        "cover_color": "#795548"
    },
    82: {
        "title": "Becoming",
        "author": "Michelle Obama",
        "genre": "Memoir",
        "year": 2018,
        "pages": 426,
        "summary": "Michelle Obama shares her journey from Chicago's South Side to the White House and beyond. An intimate, powerful memoir of identity, love, and using your voice to make a difference.",
        "read_link": "https://openlibrary.org/works/OL17930367W/Becoming",
        "cover_color": "#9c27b0"
    },
    83: {
        "title": "Sapiens",
        "author": "Yuval Noah Harari",
        "genre": "Non-Fiction",
        "year": 2011,
        "pages": 443,
        "summary": "A sweeping history of humankind from the Stone Age to the present and into the future. Harari explores how Homo sapiens came to dominate the planet through cognitive, agricultural, and scientific revolutions.",
        "read_link": "https://openlibrary.org/works/OL17075811W/Sapiens?edition=key:/books/OL26592198M",
        "cover_color": "#ff9800"
    },
    84: {
        "title": "Thinking, Fast and Slow",
        "author": "Daniel Kahneman",
        "genre": "Non-Fiction",
        "year": 2011,
        "pages": 499,
        "summary": "Nobel laureate Kahneman reveals the two systems that drive how we think and make decisions. A groundbreaking exploration of intuition, rationality, and the biases that shape our choices.",
        "read_link": "https://openlibrary.org/works/OL15992072W/Thinking_fast_and_slow?edition=key%3A/books/OL36689110M",
        "cover_color": "#607d8b"
    },
    85: {
        "title": "Atomic Habits",
        "author": "James Clear",
        "genre": "Self-Help",
        "year": 2018,
        "pages": 320,
        "summary": "Small changes can lead to remarkable results when you understand how habits work. A practical guide to breaking bad habits and building good ones through tiny adjustments that compound over time.",
        "read_link": "https://openlibrary.org/works/OL17930368W/Atomic_Habits?edition=key:/books/OL38290995M",
        "cover_color": "#ffeb3b"
    },
    86: {
        "title": "The Power of Now",
        "author": "Eckhart Tolle",
        "genre": "Self-Help",
        "year": 1997,
        "pages": 236,
        "summary": "A guide to spiritual enlightenment through living in the present moment. Tolle shares how to quiet the mind, find inner peace, and discover the transformative power of now.",
        "read_link": "https://openlibrary.org/works/OL5727686W/The_Power_of_Now?edition=key:/books/OL24294674M",
        "cover_color": "#00bcd4"
    },
    87: {
        "title": "The Subtle Art of Not Giving a F*ck",
        "author": "Mark Manson",
        "genre": "Self-Help",
        "year": 2016,
        "pages": 212,
        "summary": "A counterintuitive approach to living a good life by caring about less but caring about what matters. Manson delivers brutal honesty about values, responsibility, and what makes us happy.",
        "read_link": "https://openlibrary.org/works/OL17590212W/The_Subtle_Art_of_Not_Giving_a_F*ck?edition=key:/books/OL28230579M",
        "cover_color": "#ff5722"
    },
    88: {
        "title": "The 7 Habits of Highly Effective People",
        "author": "Stephen R. Covey",
        "genre": "Self-Help",
        "year": 1989,
        "pages": 381,
        "summary": "Covey's principles for personal effectiveness focus on character, not personality. A timeless framework for productivity, leadership, and living with integrity that has influenced millions.",
        "read_link": "https://openlibrary.org/works/OL2629977W/The_7_Habits_of_Highly_Effective_People?edition=key:/books/OL24362766M",
        "cover_color": "#4caf50"
    },
    89: {
        "title": "Rich Dad Poor Dad",
        "author": "Robert T. Kiyosaki",
        "genre": "Finance",
        "year": 1997,
        "pages": 207,
        "summary": "Lessons from two fathers teach the difference between working for money and having money work for you. A paradigm-shifting book about financial literacy, investing, and building wealth.",
        "read_link": "https://openlibrary.org/works/OL2010879W/Rich_Dad_Poor_Dad?edition=key:/books/OL27234831M",
        "cover_color": "#9c27b0"
    },
    90: {
        "title": "The Intelligent Investor",
        "author": "Benjamin Graham",
        "genre": "Finance",
        "year": 1949,
        "pages": 640,
        "summary": "The definitive book on value investing, endorsed by Warren Buffett as the best investing book ever written. Graham's timeless wisdom on market psychology and intelligent investing strategy.",
        "read_link": "https://openlibrary.org/works/OL273184W/The_Intelligent_Investor?edition=key:/books/OL59144618M",
        "cover_color": "#1976d2"
    },
    91: {
        "title": "The Lean Startup",
        "author": "Eric Ries",
        "genre": "Business",
        "year": 2011,
        "pages": 336,
        "summary": "A methodology for developing businesses and products through validated learning and rapid experimentation. Ries revolutionized how startups and corporations approach innovation and product development.",
        "read_link": "https://openlibrary.org/books/OL24982481M/The_Lean_Startup",
        "cover_color": "#4caf50"
    },
    92: {
        "title": "Zero to One",
        "author": "Peter Thiel",
        "genre": "Business",
        "year": 2014,
        "pages": 195,
        "summary": "PayPal co-founder Thiel shares contrarian thoughts on startups and building the future. A provocative guide to creating something truly new instead of copying what already exists.",
        "read_link": "https://openlibrary.org/works/OL17078706W/Zero_to_One?edition=key:/books/OL38565226M",
        "cover_color": "#3f51b5"
    },
    93: {
        "title": "Steve Jobs",
        "author": "Walter Isaacson",
        "genre": "Biography",
        "year": 2011,
        "pages": 656,
        "summary": "The authorized biography of Apple's legendary co-founder, based on extensive interviews. An intimate portrait of the visionary, perfectionist, and difficult genius who transformed multiple industries.",
        "read_link": "https://openlibrary.org/works/OL16085155W/Steve_Jobs?edition=key:/books/OL27154061M",
        "cover_color": "#212121"
    },
    94: {
        "title": "The Diary of a Young Girl",
        "author": "Anne Frank",
        "genre": "Memoir",
        "year": 1947,
        "pages": 283,
        "summary": "Anne Frank's diary chronicles two years hiding from Nazis in Amsterdam. A powerful, intimate record of adolescence and hope amidst the Holocaust that has touched millions worldwide.",
        "read_link": "https://openlibrary.org/works/OL266178W/Het_Achterhuis?edition=key:/books/OL21965847M",
        "cover_color": "#795548"
    },
    95: {
        "title": "Man's Search for Meaning",
        "author": "Viktor E. Frankl",
        "genre": "Psychology",
        "year": 1946,
        "pages": 184,
        "summary": "Psychiatrist Frankl finds meaning in suffering during the Holocaust and develops logotherapy. A profound meditation on finding purpose that has guided millions through life's darkest moments.",
        "read_link": "https://openlibrary.org/works/OL1268413W/..._Trotzdem_Ja_zum_Leben_sagen?edition=key:/books/OL58936271M",
        "cover_color": "#607d8b"
    },
    96: {
        "title": "The Art of War",
        "author": "Sun Tzu",
        "genre": "Philosophy",
        "year": -500,
        "pages": 68,
        "summary": "Ancient Chinese military strategy that has influenced warfare, business, and competition for millennia. Sun Tzu's wisdom on strategy, leadership, and winning without fighting remains eternally relevant.",
        "read_link": "https://openlibrary.org/works/OL244537W/The_Art_of_War?edition=key%3A/books/OL54172M",
        "cover_color": "#b71c1c"
    },
    97: {
        "title": "Meditations",
        "author": "Marcus Aurelius",
        "genre": "Philosophy",
        "year": 180,
        "pages": 254,
        "summary": "The Roman Emperor's private reflections on Stoic philosophy and the good life. Timeless wisdom on resilience, virtue, and finding peace that has guided leaders for two thousand years.",
        "read_link": "https://www.gutenberg.org/ebooks/2680",
        "cover_color": "#546e7a"
    },
    98: {
        "title": "Thus Spoke Zarathustra",
        "author": "Friedrich Nietzsche",
        "genre": "Philosophy",
        "year": 1883,
        "pages": 352,
        "summary": "Nietzsche's philosophical novel introduces the Ubermensch and the death of God through the prophet Zarathustra. A challenging, poetic exploration of morality, meaning, and human potential.",
        "read_link": "https://www.gutenberg.org/ebooks/1998",
        "cover_color": "#5c6bc0"
    },
    99: {
        "title": "The Republic",
        "author": "Plato",
        "genre": "Philosophy",
        "year": -375,
        "pages": 416,
        "summary": "Plato's Socratic dialogue explores justice, the ideal state, and the nature of the soul. The foundational text of Western philosophy that shaped political theory and ethics for millennia.",
        "read_link": "https://www.gutenberg.org/ebooks/1497",
        "cover_color": "#7e57c2"
    },
    100: {
        "title": "Siddhartha",
        "author": "Hermann Hesse",
        "genre": "Fiction",
        "year": 1922,
        "pages": 152,
        "summary": "A young Brahmin seeks enlightenment through different paths, from asceticism to sensual pleasure. Hesse's gentle novel explores Eastern philosophy and the journey to self-discovery and wisdom.",
        "read_link": "https://www.gutenberg.org/ebooks/2500",
        "cover_color": "#ff9800"
    }
}

def get_book_by_id(book_id):
    """Get a book by its ID"""
    return BOOKS_DATABASE.get(book_id)

def get_all_books():
    """Get all books as a list"""
    return list(BOOKS_DATABASE.values())

def get_books_by_genre(genre):
    """Get all books of a specific genre"""
    return [book for book in BOOKS_DATABASE.values() if book['genre'] == genre]

def get_all_genres():
    """Get all unique genres"""
    return list(set(book['genre'] for book in BOOKS_DATABASE.values()))
