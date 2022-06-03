import time, sys, keyboard
previous = ""
before = []
seePostMatch = False

def print_with_delay(text, ignoreSpeedUp = False):
    sys.stdout.write("\n> ")
    sys.stdout.flush()
    for c in text:
        sys.stdout.write(c)
        if (c == "\n"):
            sys.stdout.flush()
            sys.stdout.write("> ")
        sys.stdout.flush()
        time.sleep(0.04)
        if (keyboard.is_pressed("backspace") and not ignoreSpeedUp):
            sys.stdout.write(" ~XXX")
            sys.stdout.flush()
            break

def main_loop():
    global previous, seePostMatch
    restrict_words = ["\"ZAVALA SNACKS\"", "\"ZAVALA ACTION SNACKS\"", "\"TITAN VITAMINS\"", "\"EDIBLE ZAVALA\"", "\"ZAVALA ACTION VITAMINS\"", "\"VANGUARD VITAMINS\""]
    inp = input("\n\n?> ")
    inporig = inp
    inp = inp.lower()
    before.append("\"" + inporig + "\"")

    if (len(before) > 50):
        before.remove(before[0])

    if "\"" + inp.upper() + "\"" in restrict_words:
        previous = "ALL RESULTS TAGGED WITH THE FOLLOWING RELATED SEARCH QUERIES REQUIRE TWO-THIRDS VANGUARD AUTHORIZATION FOR DISCLOSURE:\n" + " ".join(str(x) for x in restrict_words)

    elif inp == "logout" or inp == "log out":
        print_with_delay("THANK YOU FOR USING THE VANGUARD TEXT-ONLY DATABASE, USER \"ACEOFHEARTS\". BE BRAVE.", True)
        time.sleep(3)
        exit(0)

    elif inp == "what were we talking about":
        if len(before) > 0:
            previous = "LAST 50 SEARCHES ACROSS ALL DEVICES, CHRONOLOGICAL:\n" + " ".join(str(x) for x in before)
        else:
            previous = "NO PREVIOUS SEARCH RESULTS ACROSS ANY DEVICES."

    elif inp == "did horse people ever exist":
        previous = "THERE ARE NO KNOWN ENCOUNTERS WITH QUADRUPED LIFE FORMS CAPABLE OF SPACE FLIGHT. SOME EARLY SIGHTINGS OF FALLEN RAIDING PARTIES MISTAKENLY IDENTIFIED THEIR METHODS OF RAPID LOCOMOTION AS EQUINE."

    elif inp == "did fallen ever ride horses":
        previous = "NO."

    elif inp == "traveler road trip snacks":
        previous = "SINCE THE TRAVELER'S FINAL EXODUS FROM IO PRIOR TO THE COLLAPSE, ECHO MESA HAS BEEN A POPULAR PILGRIMAGE DESTINATION FOR GUARDIANS. AS THE TRAVELER'S TRANSFORMATION OF THE JOVIAN MOON WAS INCOMPLETE, IO'S CLIMATE AND GEOGRAPHY DO NOT SUPPORT AGRICULTURE IN THE CONVENTIONAL SENSE. VANGUARD COMMANDER ZAVALA THEREFORE RECOMMENDS TRAVELERS PRE-PACKAGE AND BRING THEIR OWN SOURCES OF NUTRITION."

    elif inp == "traveler":
        previous = "OVER 50,000,000 RESULTS FOUND. PLEASE NARROW SEARCH CRITERIA."

    elif inp == "traveler eyeball":
        previous = "OVER 70,000,000 RESULTS FOUND. PLEASE NARROW SEARCH CRITERIA."

    elif inp == "where did the traveler come from":
        previous = "OVER 10,000,000 RESULTS FOUND. PLEASE NARROW SEARCH CRITERIA."

    elif "change what this says" in inp or "change database" in inp or "remove this" in inp:
        previous = "ADDING, ALTERING, OR REMOVING DATA FROM THE VANGUARD DATABASE REQUIRES THREE-THIRDS VANGUARD AUTHORIZATION."

    elif inp == "traveler googly eyes terminal background":
        previous = "PLEASE CONNECT TO A DEVICE WITH AN IMAGE DISPLAY TO VIEW THESE RESULTS."

    elif inp == "first article about cayde":
        previous = "THE FIRST CITY NEWS ARTICLE ABOUT 'CAYDE' WAS 126 YEARS 11 MONTHS AGO."

    elif inp == "news about cayde":
        previous = "THERE ARE 4 NEW ARTICLES SINCE YOUR LAST SEARCH 26 HOURS, 33 MINUTES AGO."

    elif inp == "beat shaxx":
        previous = "ONLY ONE GUARDIAN HAS DEFEATED LORD SHAXX IN THE CRUCIBLE. RELATED: REY, I. DO YOU WISH TO SEE POST-MATCH RESULTS?"

    elif inp == "cheat crucible":
        previous = "CRUCIBLE PARTICIPANTS ARE SUBJECT TO A STRICT CODE OF CONDUCT. CHEATERS WILL BE BANNED."

    elif inp == "ok what counts as cheating":
        previous = "TO ACT DISHONESTLY OR UNFAIRLY IN ORDER TO GAIN AN ADVANTAGE."

    elif inp == "is luck cheating":
        previous = "\"LUCK\" AND \"CHEATING\" ARE NOT EQUIVALENT."

    elif inp == "are my pants lucky":
        previous = "PROBABLY NOT."

    elif inp == "ikora current location":
        previous = "WARLOCK VANGUARD IKORA REY IS CURRENTLY IN THE UNDERWATCH. WOULD YOU LIKE TO CONTACT HER?"

    elif inp.startswith("126 years ago"):
        previous = "MAJOR EVENTS OF 126 YEARS AGO:\nSIGNIFICANT PROGRESS MADE IN FACTION ACCORDS. RELATED: BRASK, A.\nTRAVELER TRUE ORIGIN AND PURPOSE DISCOVERED\n\nMINOR EVENTS OF 126 YEARS AGO:\nFIRST 25-MATCH CRUCIBLE WINNING STREAK RECORDED. RELATED: REY, I.\nCENTAUR PLANETOID \"7066 NESSUS\" RE-ENTERS SYSTEM AFTER UNEXPLAINED DELAY. RELATED: WHERE DID THE \"EXODUS BLACK\" COLONY SHIP GO?"

    elif not inp.startswith("what??") or previous == "":
        previous = "SORRY, I DIDN'T UNDERSTAND \"" + inporig + "\"."

    print_with_delay(previous)
    main_loop()

print_with_delay("REMOTE VANGUARD DATABASE TEXT-ONLY SEARCH INITIALIZED.\nWELCOME, USER \"ACEOFHEARTS\".\nPLEASE ENTER SEARCH QUERY.", True)
main_loop()