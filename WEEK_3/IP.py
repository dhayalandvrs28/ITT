L = {"192.168.1.1", "10.0.0.5", "172.16.0.2"}
F = {"192.168.1.1", "10.0.0.8", "172.16.0.5"}
B = {"172.16.0.5", "10.0.0.10"}

both_not_blocked = (L & F) - B
print("Successful and failed but not blacklisted:", both_not_blocked)

attempted_never_succeeded = F - L
print("Attempted but never succeeded:", attempted_never_succeeded)

only_blacklisted = B - (L | F)
print("Only blacklisted and never attempted:", only_blacklisted)