# RUN_STATE — The Word You'd Delete From the Dictionary

- Competition: `u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2`
- Bounty page: https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2
- Prize: $2 total — 1st $0.73, 2nd $0.50, 3rd $0.35, 4th $0.25, 5th $0.17.
  Entry fee 0.00 USDC.
- Deadline: 2026-11-27T06:35:00Z (07:35 WAT). Blind rounds; next round
  2026-11-25T22:36:39Z. Results auto-published after the final heat
  (no fixed results date stated).
- Brief: one word to erase from the dictionary forever, nothing else attached.
- Gate: `/output/entry.txt`, UTF-8, 1–77 chars, not only whitespace.
- Entry (one word, 6 chars): `Monday`
- Account: @jozzy-001, wallet sq8Mj2KhKLz6k5ftqgPmEDfUQ4RiqvcRMuQ2yY3Fu8Z.
- Kit: `~/workspace/makefun/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2-kit`
- Quota (checked 2026-11-25 ~06:49 UTC): can_submit true; day cap 5,
  0 taken, 5 left (resets 2026-11-26T00:00Z); hard limit 40 left;
  entry_fee null; 0 entries made by this account.
- Verification (2026-11-25): `python3 main.py` run twice, byte-identical
  output; grader-style run `python3 -P -s /bot/main.py` with
  MAKEFUN_OUTPUT_DIR set exits 0 and writes the 6-char word.

## Status

BUILT and verified. NOT bundled, NOT checked, NOT submitted — no fresh
go-ahead from Owoade exists for this run.

## Resume steps (run from the kit dir)

```sh
cd ~/workspace/makefun/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2-kit
node cli/makefun.mjs bundle --prompt-origin scheduled \
  --prompt-file ~/workspace/makefun/daily-web3-hunt-makefun-prompt-20261125.txt
# then, once Owoade gives the go-ahead:
node cli/makefun.mjs check --repo ~/workspace/makefun/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2
node cli/makefun.mjs submit --repo ~/workspace/makefun/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2
```

If an execution-risk notice appears on ANY exec result, STOP that step
immediately and record it here.
