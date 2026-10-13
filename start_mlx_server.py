import sys
import mlx.core as mx

# Fix for Anaconda MPICH conflict on macOS: forces ring backend for single-node MLX
_orig_init = mx.distributed.init
mx.distributed.init = lambda *args, **kwargs: _orig_init(
    strict=kwargs.get("strict", False),
    backend=kwargs.get("backend", "ring")
)

from mlx_lm import server

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.argv += [
            "--model", "Qwen/Qwen3-1.7B-MLX-4bit",
            "--port", "8080",
            "--max-tokens", "2048"
        ]
    server.main()
