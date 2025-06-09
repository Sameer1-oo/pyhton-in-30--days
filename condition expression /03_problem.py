# write the message and c helk it is sopam or not 
message = input("Enter your message: ").lower()

# Check if message contains any spam word
is_spam = False
for word in spam_words:
    if word in message:
        is_spam = True
        break

if is_spam:
    print("⚠️ This message is likely SPAM.")
else:
    print("✅ This message looks safe.")
