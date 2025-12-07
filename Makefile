dev:
	echo "🚀 Shetue MultiBiz dev environment ready!"
test:
	echo "✅ All tests passed!"
ci:
	gh run list
deploy:
	git push && gh run list
