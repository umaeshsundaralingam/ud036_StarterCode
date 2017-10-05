import media
import fresh_tomatoes
#Create instances of class Movie here
toy_story_3 = media.Movie("Toy Story 3"
                          ,"Lee Unkrich"
                          ,"https://www.youtube.com/watch?v=JcpWXaA2qeg"
                          ,"https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg"
                          ,"17-year-old Andy is about to leave for college, and his toys have not been played with for years. He intends to take Woody with him, and puts Buzz Lightyear, Jessie and the other toys in a trash bag to be stored in the attic. Andy's mother mistakenly takes the bag to the curb for garbage pickup.")
high_school_musical = media.Movie("High School Musical"
                                  ,"Kenny Ortega"
                                  ,"https://www.youtube.com/watch?v=ukDLkkvZYFk"
                                  ,"https://upload.wikimedia.org/wikipedia/en/a/a5/HSMposter.jpg"
                                  ,"On New Year's Eve in 2006, high school juniors Troy Bolton (Zac Efron) and Gabriella Montez (Vanessa Hudgens) meet at a party while both teens are at a ski lodge during winter break. At the party, the two are called upon to sing karaoke together. They find that they have a connection and decide to exchange numbers before going their separate ways.")

lion_king = media.Movie("Lion King"
                        ,"Rob Minkoff & Roger Allers"
                        ,"https://www.youtube.com/watch?v=4sj1MT05lAA"
                        ,"https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg"
                        ,"In the Pride Lands of Africa, a lion rules over the animal kingdom from Pride Rock. King Mufasa's newborn son, Simba, is presented to the assembled animals by Rafiki, a mandrill who serves as shaman and advisor. Mufasa shows young Simba the Pride Lands and explains to him the responsibilities of kingship and the \"circle of life\", which connects all living things. Mufasa's younger brother, Scar, covets the throne, and plots to kill Mufasa and Simba, so he can become king.")

disney_hercules = media.Movie("Disneys Hercules"
                              ,"Ron Clements & John Musker"
                              ,"https://www.youtube.com/watch?v=yIAvF8hFEYM"
                              ,"https://upload.wikimedia.org/wikipedia/en/6/65/Hercules_%281997_film%29_poster.jpg"
                              ,"After imprisoning the Titans beneath the ocean, the Greek gods Zeus and his wife, Hera, have a son named Hercules. While the other gods are joyful, Zeus' jealous brother Hades plots to overthrow Zeus and rule Mount Olympus. Turning to the Fates for help, Hades learns that in eighteen years, a planetary alignment will allow him to locate and free the Titans to conquer Olympus, but only if Hercules does not interfere. Hades sends his minions Pain and Panic to dispose of Hercules. The two succeed at kidnapping the infant and feeding him a formula that turns him mortal, but fail to remove his superhuman strength before Hercules is found and adopted by the farmers Amphitryon and Alcmene.")

aladdin = media.Movie("Aladdin"
                      ,"Ron Clements & John Musker"
                      ,"https://www.youtube.com/watch?v=QapaqcDucmg"
                      ,"https://upload.wikimedia.org/wikipedia/en/5/58/Aladdinposter.jpg"
                      ,"In the city of Agrabah, Jafar, the Grand vizier of the Sultan, and his parrot Iago, seek the lamp hidden within the Cave of Wonders, but are told that only a \"diamond in the rough\" may enter. Jafar identifies a street urchin named Aladdin. Aladdin and his pet monkey, Abu, meet Princess Jasmine, who refuses to marry a suitor and temporarily leaves the palace. Aladdin and Jasmine become friends and fall in love. When the palace guards capture Aladdin, Jafar lies to Jasmine that Aladdin has been executed.")

prince_of_persia = media.Movie("Prince of Persia"
                               ,"Mike Newell"
                               ,"https://www.youtube.com/watch?v=ZgEt-4L3fKQ"
                               ,"https://upload.wikimedia.org/wikipedia/en/d/df/Prince_of_Persia_poster.jpg"
                               ,"Dastan, a street urchin in Persia, is adopted by King Sharaman after showing courage in the marketplace. Fifteen years later, Sharaman's brother Nizam receives proof that the holy city of Alamut is supplying weapons to Persian enemies, and the princes — Dastan, along with the king's biological sons Tus and Garsiv — are sent to siege and take over Alamut. Dastan and his friends breach into the city on their own, and open a gate letting the Persians in. During the attack, Dastan fights a guard for Alamut's royal family and takes from him a special dagger.")
#Instantiate and store instances of Movie in array
movies = [toy_story_3, high_school_musical, lion_king, disney_hercules, aladdin, prince_of_persia]
print(movies)
fresh_tomatoes.open_movies_page(movies)


